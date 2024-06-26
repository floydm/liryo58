// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
     /* 
      # HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----#SPACE--#SPACE--# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----
     QWERTY */
    [0] = LAYOUT(
      KC_GRV,   KC_1,     KC_2,     KC_3,     KC_4,     KC_5,                                         KC_6,     KC_7,     KC_8,     KC_9,     KC_0,     KC_BSPC,
      KC_TAB,   KC_Q,     KC_W,     KC_E,     KC_R,     KC_T,                                         KC_Y,     KC_U,     KC_I,     KC_O,     KC_P,     KC_MINS,
      KC_ESC,   KC_A,     KC_S,     KC_D,     KC_F,     KC_G,                                         KC_H,     KC_J,     KC_K,     KC_L,     KC_SCLN,  KC_QUOT,
      KC_LSFT,  KC_Z,     KC_X,     KC_C,     KC_V,     KC_B,                                         KC_N,     KC_M,     KC_COMM,  KC_DOT,   KC_SLSH,  KC_RSFT,
                          KC_LCTL,  KC_LGUI,  KC_LALT,  MO(1),    KC_SPC,                   KC_ENT,   MO(2),    KC_RALT,  KC_RGUI,  KC_RCTL
    ),
    /* Lower */
    [1] = LAYOUT(
      _______,  KC_F1,    KC_F2,    KC_F3,    KC_F4,    KC_F5,                                        KC_F6,    KC_F7,    KC_F8,    KC_F9,    KC_F10,   KC_F11,
      _______,  _______,  _______,  _______,  _______,  _______,                                      _______,  _______,  _______,  _______,  _______,  KC_F12,
      _______,  KC_EXLM,  KC_AT,    KC_HASH,  KC_DLR,   KC_PERC,                                      KC_CIRC,  KC_AMPR,  KC_ASTR,  KC_LPRN,  KC_RPRN,  KC_PIPE,
      _______,  KC_EQL,   KC_MINS,  KC_PLUS,  KC_LCBR,  KC_RCBR,                                      KC_LBRC,  KC_RBRC,  KC_SCLN,  KC_COLN,  KC_BSLS,  _______,
                          _______,  _______,  _______,  _______,  _______,                  _______,  _______,  _______,  _______,  _______
    ),
    /* Upper */
    [2] = LAYOUT(
      _______,  _______,  _______,  _______,  _______,  _______,                                      _______,  _______,  _______,  _______,  _______,  KC_DEL,
      _______,  _______,  _______,  _______,  _______,  _______,                                      KC_PGUP,  KC_HOME,  KC_UP,    KC_END,   _______,  _______,
      _______,  _______,  _______,  _______,  _______,  _______,                                      KC_PGDN,  KC_LEFT,  KC_DOWN,  KC_RIGHT, _______,  KC_PSCR,
      _______,  _______,  _______,  _______,  _______,  _______,                                      TG(4),  _______,  _______,  _______,  _______,  _______,
                          _______,  _______,  _______,  _______,  _______,                  _______,  _______,  _______,  _______,  _______
    ),
    /* Adjust */
    [3] = LAYOUT(
      _______,  _______,  _______,  _______,  _______,  _______,                                      _______,  _______,  _______,  _______,  _______,  _______,
      _______,  _______,  _______,  _______,  _______,  _______,                                      _______,  _______,  _______,  _______,  _______,  _______,
      _______,  _______,  _______,  _______,  _______,  _______,                                      _______,  _______,  _______,  _______,  _______,  _______,
      _______,  _______,  _______,  _______,  _______,  _______,                                      _______,  _______,  _______,  _______,  _______,  _______,
                          _______,  _______,  _______,  _______,  _______,                  _______,  _______,  _______,  _______,  _______
    ),
    /* Gaming */
    [4] = LAYOUT(
      _______,  KC_1,     KC_2,     KC_3,     KC_4,     KC_5,                                         _______,  _______,  _______,  _______,  _______,  _______,
      _______,  KC_T,     KC_Q,     KC_W,     KC_E,     KC_R,                                         _______,  _______,  _______,  _______,  _______,  _______,
      _______,  KC_G,     KC_A,     KC_S,     KC_D,     KC_F,                                         _______,  _______,  _______,  _______,  _______,  _______,
      _______,  KC_Z,     KC_X,     KC_C,     KC_V,     KC_B,                                         _______,  _______,  _______,  _______,  _______,  _______,
                          MO(1),    KC_DEL,   KC_LALT,  KC_LCTL,  KC_SPC,                   _______,  _______,  _______,  _______,  _______
    ),
    [5] = LAYOUT(
      _______,  _______,  _______,  _______,  _______,  _______,                                      _______,  _______,  _______,  _______,  _______,  _______,
      _______,  _______,  _______,  _______,  _______,  _______,                                      _______,  _______,  _______,  _______,  _______,  _______,
      _______,  _______,  _______,  _______,  _______,  _______,                                      _______,  _______,  _______,  _______,  _______,  _______,
      _______,  _______,  _______,  _______,  _______,  _______,                                      _______,  _______,  _______,  _______,  _______,  _______,
                          _______,  _______,  _______,  _______,  _______,                  _______,  _______,  _______,  _______,  _______
    ),
    [6] = LAYOUT(
      _______,  _______,  _______,  _______,  _______,  _______,                                      _______,  _______,  _______,  _______,  _______,  _______,
      _______,  _______,  _______,  _______,  _______,  _______,                                      _______,  _______,  _______,  _______,  _______,  _______,
      _______,  _______,  _______,  _______,  _______,  _______,                                      _______,  _______,  _______,  _______,  _______,  _______,
      _______,  _______,  _______,  _______,  _______,  _______,                                      _______,  _______,  _______,  _______,  _______,  _______,
                          _______,  _______,  _______,  _______,  _______,                  _______,  _______,  _______,  _______,  _______
    ),
    [7] = LAYOUT(
      _______,  _______,  _______,  _______,  _______,  _______,                                      _______,  _______,  _______,  _______,  _______,  _______,
      _______,  _______,  _______,  _______,  _______,  _______,                                      _______,  _______,  _______,  _______,  _______,  _______,
      _______,  _______,  _______,  _______,  _______,  _______,                                      _______,  _______,  _______,  _______,  _______,  _______,
      _______,  _______,  _______,  _______,  _______,  _______,                                      _______,  _______,  _______,  _______,  _______,  _______,
                          _______,  _______,  _______,  _______,  _______,                  _______,  _______,  _______,  _______,  _______
    )
};

uint16_t get_tapping_term(uint16_t keycode, keyrecord_t *record) {
    switch (keycode) {
        case LSFT_T(KC_SPC):
            return TAPPING_TERM + 1250;
        default:
            return TAPPING_TERM;
    }
}

void keyboard_post_init_user(void) {
  // Call the post init code.
  rgblight_enable_noeeprom(); // enables Rgb, without saving settings
  rgblight_sethsv_noeeprom(169, 255, 10); // sets the color to teal/cyan without saving
}

layer_state_t layer_state_set_user(layer_state_t state) {
    switch (get_highest_layer(state)) {
    case 1:
        rgblight_sethsv_noeeprom (127,  255, 10);  // Cyan
        break;
    case 2:
        rgblight_sethsv_noeeprom (106,  255, 10);  // Spring Green
        break;
    case 3:
        rgblight_sethsv_noeeprom (43,  255, 10); // Yellow
        break;
    case 4:
        rgblight_sethsv_noeeprom (148,  255, 10); // Azure
        break;
    case 5:
        rgblight_sethsv_noeeprom (21,  255, 10); // Orange
        break;
    case 6:
        rgblight_sethsv_noeeprom (0,  255, 10); // Red
        break;
    case 7:
        rgblight_sethsv_noeeprom (180,  255, 10); // Violet
        break;
    default: //  for any other layers, or the default layer
        rgblight_sethsv_noeeprom(169, 255, 10);
        break;
    }
  return state;
};

void refresh_rgb(void) {
    key_timer = timer_read32(); // store time of last refresh
    if (is_rgb_timeout)
    {
        is_rgb_timeout = false;
        rgblight_wakeup();
    }
}
void check_rgb_timeout(void) {
    if (!is_rgb_timeout && timer_elapsed32(key_timer) > RGBLIGHT_TIMEOUT) // check if RGB has already timeout and if enough time has passed
    {
        rgblight_suspend();
        is_rgb_timeout = true;
    }
}
/* Then, call the above functions from QMK's built in post processing functions like so */
/* Runs at the end of each scan loop, check if RGB timeout has occured or not */
void housekeeping_task_user(void) {
#ifdef RGBLIGHT_TIMEOUT
    check_rgb_timeout();
#endif
}
/* Runs after each key press, check if activity occurred */
void post_process_record_user(uint16_t keycode, keyrecord_t *record) {
#ifdef RGBLIGHT_TIMEOUT
    if (record->event.pressed)
        refresh_rgb();
#endif
}
/* Runs after each encoder tick, check if activity occurred */
void post_encoder_update_user(uint8_t index, bool clockwise) {
#ifdef RGBLIGHT_TIMEOUT
    refresh_rgb();
#endif
}

