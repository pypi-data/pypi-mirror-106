/*
 * Copyright 2014-2021 Jetperch LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "fitterbap/host/comm.h"
#include "fitterbap/host/uart_thread.h"
#include "fitterbap/comm/data_link.h"
#include "fitterbap/pubsub.h"
#include "fitterbap/comm/stack.h"
#include "fitterbap/os/mutex.h"
#include "fitterbap/ec.h"
#include "fitterbap/log.h"
#include "fitterbap/platform.h"
#include "fitterbap/time.h"
#include <stdio.h>
#include <windows.h>


// On a host computer, make plenty big
#define PUBSUB_BUFFER_SIZE (2000000)
#define PUBSUB_PREFIX "h/"
#define PORT0_PREFIX PUBSUB_PREFIX "c/"


struct fbp_comm_s {
    struct fbp_stack_s * stack;
    struct fbp_uartt_s * uart;
    struct fbp_pubsub_s * pubsub;
    fbp_os_mutex_t pubsub_mutex;
    struct fbp_evm_api_s evm_api;
    fbp_pubsub_subscribe_fn subscriber_fn;
    void * subscriber_user_data;
};

static void ll_send(void * user_data, uint8_t const * buffer, uint32_t buffer_size) {
    struct fbp_comm_s * self = (struct fbp_comm_s *) user_data;
    if (fbp_uartt_send_available(self->uart) >= buffer_size) {
        fbp_uartt_send(self->uart, buffer, buffer_size);
    }
}

static uint32_t ll_send_available(void * user_data) {
    struct fbp_comm_s * self = (struct fbp_comm_s *) user_data;
    return fbp_uartt_send_available(self->uart);
}

static void on_uart_recv(void *user_data, uint8_t *buffer, uint32_t buffer_size) {
    struct fbp_comm_s * self = (struct fbp_comm_s *) user_data;
    fbp_dl_ll_recv(self->stack->dl, buffer, buffer_size);
}

static void on_pubsub_process(void * user_data, int32_t event_id) {
    (void) event_id;
    struct fbp_comm_s * self = (struct fbp_comm_s *) user_data;
    fbp_pubsub_process(self->pubsub);
}

static void on_publish_fn(void * user_data) {
    struct fbp_comm_s * self = (struct fbp_comm_s *) user_data;
    self->evm_api.schedule(self->evm_api.evm, 0, on_pubsub_process, self);
}

static void on_port_recv_default(void *user_data,
                                 uint8_t port_id,
                                 enum fbp_transport_seq_e seq,
                                 uint16_t port_data,
                                 uint8_t *msg, uint32_t msg_size) {
    char topic[FBP_PUBSUB_TOPIC_LENGTH_MAX];
    struct fbp_comm_s * self = (struct fbp_comm_s *) user_data;
    if (msg_size > FBP_FRAMER_PAYLOAD_MAX_SIZE) {
        return;
    }

    // Construct topic string
    char * src = PORT0_PREFIX;
    char * t = topic;
    while (*src) {
        *t++ = *src++;
    }
    if (port_id >= 10) {
        *t++ = '0' + (port_id / 10);
    }
    *t++ = '0' + (port_id % 10);
    src = "/din";
    while (*src) {
        *t++ = *src++;
    }
    *t = 0;

    if (seq != FBP_TRANSPORT_SEQ_SINGLE) {
        FBP_LOGW("unexpected seq %d on port %d", (int) seq, (int) port_id);
    }
    if (port_data) {
        // todo handle decompression
    }
    fbp_pubsub_publish(self->pubsub, topic, &fbp_union_bin(msg, msg_size), NULL, NULL);
}

struct fbp_comm_s * fbp_comm_initialize(struct fbp_dl_config_s const * config,
                                        const char * device,
                                        uint32_t baudrate,
                                        fbp_pubsub_subscribe_fn cbk_fn,
                                        void * cbk_user_data) {
    if (!cbk_fn) {
        FBP_LOGW("Must provide cbk_fn");
        return NULL;
    }
    struct fbp_comm_s * self = fbp_alloc_clr(sizeof(struct fbp_comm_s));
    if (!self) {
        return NULL;
    }

    FBP_LOGI("fbp_comm_initialize(%s, %d)", device, (int) baudrate);
    self->subscriber_fn = cbk_fn;
    self->subscriber_user_data = cbk_user_data;
    self->pubsub = fbp_pubsub_initialize(PUBSUB_PREFIX, PUBSUB_BUFFER_SIZE);
    if (!self->pubsub) {
        goto on_error;
    }

    self->pubsub_mutex = fbp_os_mutex_alloc();
    if (!self->pubsub_mutex) {
        goto on_error;
    }
    fbp_pubsub_register_mutex(self->pubsub, self->pubsub_mutex);
    fbp_pubsub_subscribe(self->pubsub, "",
                         FBP_PUBSUB_SFLAG_RETAIN | FBP_PUBSUB_SFLAG_RSP,
                         self->subscriber_fn, self->subscriber_user_data);

    struct fbp_dl_ll_s ll = {
            .user_data = self,
            .send = ll_send,
            .send_available = ll_send_available,
    };

    struct uart_config_s uart_config = {
            .baudrate = baudrate,
            .send_size_total = 3 * FBP_FRAMER_MAX_SIZE,
            .buffer_size = FBP_FRAMER_MAX_SIZE,
            .recv_buffer_count = 16,
            .recv_fn = on_uart_recv,
            .recv_user_data = self,
    };

    self->uart = fbp_uartt_initialize(device, &uart_config);
    if (!self->uart) {
        goto on_error;
    }

    fbp_uartt_evm_api(self->uart, &self->evm_api);
    fbp_pubsub_register_on_publish(self->pubsub, on_publish_fn, self);

    self->stack = fbp_stack_initialize(config, FBP_PORT0_MODE_SERVER, PORT0_PREFIX, &self->evm_api, &ll, self->pubsub);
    if (!self->stack) {
        goto on_error;
    }
    fbp_transport_port_register_default(self->stack->transport, NULL, on_port_recv_default, self);

    if (fbp_uartt_start(self->uart, (fbp_uartt_process_fn) fbp_stack_process, self->stack)) {
        goto on_error;
    }

    fbp_os_mutex_t mutex;
    fbp_uartt_mutex(self->uart, &mutex);
    fbp_stack_mutex_set(self->stack, mutex);

    return self;

on_error:
    FBP_LOGE("fbp_comm_initialize failed");
    fbp_comm_finalize(self);
    return NULL;
}

void fbp_comm_finalize(struct fbp_comm_s * self) {
    if (self) {
        fbp_uartt_stop(self->uart);
        if (self->stack) {
            fbp_stack_finalize(self->stack);
            self->stack = NULL;
        }
        if (self->uart) {
            fbp_uartt_finalize(self->uart);
            self->uart = NULL;
        }
        if (self->pubsub) {
            fbp_pubsub_finalize(self->pubsub);
            self->pubsub = NULL;
        }
        if (self->pubsub_mutex) {
            fbp_os_mutex_free(self->pubsub_mutex);
            self->pubsub_mutex = NULL;
        }
        fbp_free(self);
    }
}

int32_t fbp_comm_publish(struct fbp_comm_s * self,
                          const char * topic, const struct fbp_union_s * value) {
    FBP_LOGI("publish(topic=%s, value.type=%d, value.size=%d)",
              topic, (int) value->type, (int) value->size);
    return fbp_pubsub_publish(self->pubsub, topic, value, self->subscriber_fn, self->subscriber_user_data);
}

int32_t fbp_comm_query(struct fbp_comm_s * self, const char * topic, struct fbp_union_s * value) {
    return fbp_pubsub_query(self->pubsub, topic, value);
}

int32_t fbp_comm_status_get(
        struct fbp_comm_s * self,
        struct fbp_dl_status_s * status) {
    return fbp_dl_status_get(self->stack->dl, status);
}
