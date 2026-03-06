/*
 * STM32 reference firmware for weedbot control path.
 *
 * Data path:
 * ROS2 control node -> UART (USB-TTL) -> STM32 -> DAC8563 -> galvo amps -> laser
 *
 * Protocol (ASCII, line based):
 *   $ARM,<0|1>*CS
 *   $SHOT,<seq>,<dac_x>,<dac_y>,<settle_us>,<fire_us>,<power_permille>*CS
 *   $PING,<seq>*CS
 *
 * Checksum CS is XOR over payload bytes (text between '$' and '*'), rendered as 2 hex chars.
 *
 * Integrate with CubeMX by:
 * 1) Assigning huart1/hspi1/htim2/htim3 handles.
 * 2) Mapping DAC sync and laser GPIO pins.
 * 3) Calling laser_controller_init() once.
 * 4) Calling laser_controller_task() in the main loop.
 */

#include "main.h"

#include <ctype.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

extern UART_HandleTypeDef huart1;
extern SPI_HandleTypeDef hspi1;
extern TIM_HandleTypeDef htim2;  // Configure as 1 MHz free-running timer.
extern TIM_HandleTypeDef htim3;  // PWM timer for laser power.

#define RX_BUF_LEN 128U
#define TX_BUF_LEN 96U

// Update these pin mappings for your board.
#define DAC_SYNC_GPIO_Port GPIOB
#define DAC_SYNC_Pin GPIO_PIN_12
#define LASER_EN_GPIO_Port GPIOA
#define LASER_EN_Pin GPIO_PIN_8
#define LASER_PWM_CHANNEL TIM_CHANNEL_1

// DAC8563 command field values (DB21:DB19), from TI datasheet.
#define DAC_CMD_WRITE_UPDATE_N 0x3U
#define DAC_ADDR_A 0x0U
#define DAC_ADDR_B 0x1U

static bool g_armed = false;
static char g_rx_buf[RX_BUF_LEN];
static uint16_t g_rx_len = 0U;

static void uart_send_line(const char *text);
static void send_ack_u32(uint32_t seq);
static void send_err_u32(uint32_t seq, const char *reason);
static bool parse_u32(const char *text, uint32_t *value_out);
static uint8_t xor_checksum(const char *payload);
static bool parse_hex_byte(const char *text, uint8_t *value_out);
static void handle_frame(char *frame);
static void process_payload(char *payload);
static void dac8563_write_channel(uint8_t channel, uint16_t value);
static void set_laser_power_permille(uint16_t power_permille);
static void set_laser_enable(bool enable);
static void delay_us(uint32_t us);
static void execute_shot(
    uint16_t dac_x,
    uint16_t dac_y,
    uint32_t settle_us,
    uint32_t fire_us,
    uint16_t power_permille
);

void laser_controller_init(void)
{
    HAL_GPIO_WritePin(LASER_EN_GPIO_Port, LASER_EN_Pin, GPIO_PIN_RESET);
    HAL_TIM_Base_Start(&htim2);
    HAL_TIM_PWM_Start(&htim3, LASER_PWM_CHANNEL);
    set_laser_power_permille(0U);
    g_armed = false;
    uart_send_line("BOOT,READY");
}

void laser_controller_task(void)
{
    uint8_t byte = 0U;
    while (HAL_UART_Receive(&huart1, &byte, 1U, 0U) == HAL_OK) {
        if (byte == '\r') {
            continue;
        }
        if (byte == '\n') {
            if (g_rx_len > 0U) {
                g_rx_buf[g_rx_len] = '\0';
                handle_frame(g_rx_buf);
                g_rx_len = 0U;
            }
            continue;
        }
        if (g_rx_len < (RX_BUF_LEN - 1U)) {
            g_rx_buf[g_rx_len++] = (char)byte;
        } else {
            g_rx_len = 0U;
            send_err_u32(0U, "RX_OVERFLOW");
        }
    }
}

static void handle_frame(char *frame)
{
    if (frame[0] != '$') {
        return;
    }

    char *star = strchr(frame, '*');
    if (star == NULL || star <= (frame + 1)) {
        send_err_u32(0U, "FRAME");
        return;
    }

    uint8_t rx_checksum = 0U;
    if (!parse_hex_byte(star + 1, &rx_checksum)) {
        send_err_u32(0U, "BAD_CS_FMT");
        return;
    }

    *star = '\0';
    char *payload = frame + 1;
    uint8_t calc_checksum = xor_checksum(payload);
    if (calc_checksum != rx_checksum) {
        send_err_u32(0U, "CS_MISMATCH");
        return;
    }

    process_payload(payload);
}

static void process_payload(char *payload)
{
    char *save_ptr = NULL;
    char *cmd = strtok_r(payload, ",", &save_ptr);
    if (cmd == NULL) {
        send_err_u32(0U, "EMPTY");
        return;
    }

    if (strcmp(cmd, "ARM") == 0) {
        char *state_text = strtok_r(NULL, ",", &save_ptr);
        uint32_t state = 0U;
        if (state_text == NULL || !parse_u32(state_text, &state)) {
            send_err_u32(0U, "ARM_ARG");
            return;
        }
        g_armed = (state != 0U);
        send_ack_u32(0U);
        return;
    }

    if (strcmp(cmd, "PING") == 0) {
        char *seq_text = strtok_r(NULL, ",", &save_ptr);
        uint32_t seq = 0U;
        if (seq_text == NULL || !parse_u32(seq_text, &seq)) {
            send_err_u32(0U, "PING_ARG");
            return;
        }
        send_ack_u32(seq);
        return;
    }

    if (strcmp(cmd, "SHOT") == 0) {
        char *seq_text = strtok_r(NULL, ",", &save_ptr);
        char *dac_x_text = strtok_r(NULL, ",", &save_ptr);
        char *dac_y_text = strtok_r(NULL, ",", &save_ptr);
        char *settle_text = strtok_r(NULL, ",", &save_ptr);
        char *fire_text = strtok_r(NULL, ",", &save_ptr);
        char *power_text = strtok_r(NULL, ",", &save_ptr);

        uint32_t seq = 0U;
        uint32_t dac_x = 0U;
        uint32_t dac_y = 0U;
        uint32_t settle_us = 0U;
        uint32_t fire_us = 0U;
        uint32_t power_permille = 0U;

        if (seq_text == NULL || dac_x_text == NULL || dac_y_text == NULL ||
            settle_text == NULL || fire_text == NULL || power_text == NULL) {
            send_err_u32(0U, "SHOT_ARG_COUNT");
            return;
        }

        if (!parse_u32(seq_text, &seq) || !parse_u32(dac_x_text, &dac_x) ||
            !parse_u32(dac_y_text, &dac_y) || !parse_u32(settle_text, &settle_us) ||
            !parse_u32(fire_text, &fire_us) || !parse_u32(power_text, &power_permille)) {
            send_err_u32(0U, "SHOT_ARG_FMT");
            return;
        }

        if (!g_armed) {
            send_err_u32(seq, "DISARMED");
            return;
        }

        if (dac_x > 65535U || dac_y > 65535U || power_permille > 1000U ||
            settle_us > 1000000U || fire_us > 1000000U) {
            send_err_u32(seq, "SHOT_RANGE");
            return;
        }

        execute_shot(
            (uint16_t)dac_x,
            (uint16_t)dac_y,
            settle_us,
            fire_us,
            (uint16_t)power_permille
        );
        send_ack_u32(seq);
        return;
    }

    send_err_u32(0U, "UNKNOWN_CMD");
}

static void execute_shot(
    uint16_t dac_x,
    uint16_t dac_y,
    uint32_t settle_us,
    uint32_t fire_us,
    uint16_t power_permille
)
{
    dac8563_write_channel(DAC_ADDR_A, dac_x);
    dac8563_write_channel(DAC_ADDR_B, dac_y);
    delay_us(settle_us);

    set_laser_power_permille(power_permille);
    set_laser_enable(true);
    delay_us(fire_us);
    set_laser_enable(false);
}

static void dac8563_write_channel(uint8_t channel, uint16_t value)
{
    uint32_t word = ((uint32_t)DAC_CMD_WRITE_UPDATE_N << 19) |
                    ((uint32_t)(channel & 0x07U) << 16) |
                    (uint32_t)value;

    uint8_t tx[3];
    tx[0] = (uint8_t)((word >> 16) & 0xFFU);
    tx[1] = (uint8_t)((word >> 8) & 0xFFU);
    tx[2] = (uint8_t)(word & 0xFFU);

    HAL_GPIO_WritePin(DAC_SYNC_GPIO_Port, DAC_SYNC_Pin, GPIO_PIN_RESET);
    HAL_SPI_Transmit(&hspi1, tx, 3U, HAL_MAX_DELAY);
    HAL_GPIO_WritePin(DAC_SYNC_GPIO_Port, DAC_SYNC_Pin, GPIO_PIN_SET);
}

static void set_laser_power_permille(uint16_t power_permille)
{
    if (power_permille > 1000U) {
        power_permille = 1000U;
    }
    uint32_t period = __HAL_TIM_GET_AUTORELOAD(&htim3) + 1U;
    uint32_t pulse = (period * (uint32_t)power_permille) / 1000U;
    __HAL_TIM_SET_COMPARE(&htim3, LASER_PWM_CHANNEL, pulse);
}

static void set_laser_enable(bool enable)
{
    HAL_GPIO_WritePin(
        LASER_EN_GPIO_Port,
        LASER_EN_Pin,
        enable ? GPIO_PIN_SET : GPIO_PIN_RESET
    );
}

static void delay_us(uint32_t us)
{
    uint32_t start = __HAL_TIM_GET_COUNTER(&htim2);
    while ((__HAL_TIM_GET_COUNTER(&htim2) - start) < us) {
    }
}

static uint8_t xor_checksum(const char *payload)
{
    uint8_t value = 0U;
    while (*payload != '\0') {
        value ^= (uint8_t)(*payload);
        payload++;
    }
    return value;
}

static bool parse_hex_byte(const char *text, uint8_t *value_out)
{
    if (text == NULL || value_out == NULL) {
        return false;
    }

    if (!isxdigit((unsigned char)text[0]) || !isxdigit((unsigned char)text[1])) {
        return false;
    }

    char tmp[3];
    tmp[0] = text[0];
    tmp[1] = text[1];
    tmp[2] = '\0';

    char *end_ptr = NULL;
    unsigned long value = strtoul(tmp, &end_ptr, 16);
    if (end_ptr == NULL || *end_ptr != '\0' || value > 0xFFUL) {
        return false;
    }
    *value_out = (uint8_t)value;
    return true;
}

static bool parse_u32(const char *text, uint32_t *value_out)
{
    if (text == NULL || value_out == NULL || *text == '\0') {
        return false;
    }
    char *end_ptr = NULL;
    unsigned long value = strtoul(text, &end_ptr, 10);
    if (end_ptr == NULL || *end_ptr != '\0') {
        return false;
    }
    *value_out = (uint32_t)value;
    return true;
}

static void send_ack_u32(uint32_t seq)
{
    char line[TX_BUF_LEN];
    (void)snprintf(line, sizeof(line), "ACK,%lu", (unsigned long)seq);
    uart_send_line(line);
}

static void send_err_u32(uint32_t seq, const char *reason)
{
    char line[TX_BUF_LEN];
    (void)snprintf(
        line,
        sizeof(line),
        "ERR,%lu,%s",
        (unsigned long)seq,
        reason != NULL ? reason : "UNKNOWN"
    );
    uart_send_line(line);
}

static void uart_send_line(const char *text)
{
    if (text == NULL) {
        return;
    }
    HAL_UART_Transmit(&huart1, (uint8_t *)text, (uint16_t)strlen(text), 50U);
    HAL_UART_Transmit(&huart1, (uint8_t *)"\n", 1U, 50U);
}
