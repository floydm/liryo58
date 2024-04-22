// Copyright 2024 Floyd Maloto (@floydm)
// SPDX-License-Identifier: GPL-2.0-or-later

#pragma once

#define EE_HANDS
#define SERIAL_USART_FULL_DUPLEX   // Enable full duplex operation mode.
#define SERIAL_USART_TX_PIN GP0     // USART TX pin
#define SERIAL_USART_RX_PIN GP1     // USART RX pin

#define RGBLIGHT_LAYERS
/*
#define BACKLIGHT_LED_COUNT 1
#define BACKLIGHT_PIN GP23
*/

/*
 * Feature disable options
 *  These options are also useful to firmware size reduction.
 */

/* disable debug print */
//#define NO_DEBUG

/* disable print */
//#define NO_PRINT

/* disable action features */
//#define NO_ACTION_LAYER
//#define NO_ACTION_TAPPING
//#define NO_ACTION_ONESHOT
