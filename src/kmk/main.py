print("Starting Liryo58 v1")

import board
import gc

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

# import modules
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.modules.combos import Combos, Chord, Sequence
from kmk.modules.holdtap import HoldTap
from kmk.modules.tapdance import TapDance

# import extensions
from kmk.extensions.rgb import RGB

keyboard = KMKKeyboard()

# Column Pins here
keyboard.col_pins = (
    board.GP10,
    board.GP11,
    board.GP12,
    board.GP13,
    board.GP14,
    board.GP15
)

# Row Pins here
keyboard.row_pins = (
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP8,
    board.GP9
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.coord_mapping = [
 0,  1,  2,  3,  4,  5,    35, 34, 33, 32, 31, 30,
 6,  7,  8,  9, 10, 11,    41, 40, 39, 38, 37, 36,
12, 13, 14, 15, 16, 17,    47, 46, 45, 44, 43, 42,
18, 19, 20, 21, 22, 23,    53, 52, 51, 50, 49, 48,
    25, 26, 27, 28, 29,    59, 58, 57, 56, 55
]

split = Split(
    split_flip=True,  # If both halves are the same, but flipped, set this True
    split_type=SplitType.UART,  # Defaults to UART
    uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
    data_pin=board.GP1,  # The primary data pin to talk to the secondary device with
    data_pin2=board.GP0,  # Second uart pin to allow 2 way communication
    use_pio=False,  # allows for UART to be used with PIO
)
layers = Layers()
combos = Combos()
holdtap = HoldTap()
tapdance = TapDance()

# RGB Stuff
sat = 255
val = 5

rgb = RGB(
    pixel_pin=board.GP23,
    num_pixels=1,
    hue_default=130,
    sat_default=sat,
    val_default=val
)

# Append extensions and modules
keyboard.extensions = [rgb]
keyboard.modules = [layers, split, combos, holdtap, tapdance]

XXXXXXX = KC.NO
_______ = KC.TRNS
LOWER = KC.MO(1)
RAISE = KC.MO(2)

keyboard.keymap = [
    [  # QWERTY
        # HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----#ENCODER--#ENCODER--# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----
        KC.GRV,   KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,                                            KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.BSPC,
        KC.TAB,   KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,                                             KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,     KC.MINS,
        KC.ESC,   KC.A,     KC.S,     KC.D,     KC.F,     KC.G,                                             KC.H,     KC.J,     KC.K,     KC.L,     KC.SCLN,  KC.QUOT,
        KC.LSFT,  KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,                                             KC.N,     KC.M,     KC.COMM,  KC.DOT,   KC.SLSH,  KC.RSFT,
                            KC.LCTL,  KC.LALT,  KC.LGUI,  LOWER,    KC.SPC,                       KC.ENT,   RAISE,    KC.RGUI,  KC.RALT,  KC.RCTL,
    ],
    [  #LOWER
        # HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----#ENCODER--#ENCODER--# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----
        XXXXXXX,  KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,                                            KC.F6,    KC.F7,    KC.F8,    KC.F9,    KC.F10,   KC.F11,
        KC.GRV,   KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,                                            KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.F12,
        XXXXXXX,  KC.EXLM,  KC.AT,    KC.HASH,  KC.DLR,   KC.PERC,                                          KC.CIRC,  KC.AMPR,  KC.ASTR,  KC.LPRN,  KC.RPRN,  KC.PIPE,
        XXXXXXX,  KC.EQL,   KC.MINS,  KC.PLUS,  KC.LCBR,  KC.RCBR,                                          KC.LBRC,  KC.RBRC,  KC.SCLN,  KC.COLN,  KC.BSLS,  XXXXXXX,
                            _______,  _______,  _______,  _______,  _______,                      _______,  _______,  _______,  _______,  _______,
    ],
    [  #RAISE
        # HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----#ENCODER--#ENCODER--# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                                          XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  KC.DEL,
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                                          KC.PGUP,  KC.HOME,    KC.UP,   KC.END,  XXXXXXX,  KC.BSPC,
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                                          KC.PGDN,  KC.LEFT,  KC.DOWN,  KC.RGHT,   KC.DEL,  KC.BSPC,
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                                          XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
                            _______,  _______,  _______,  _______,  _______,                      _______,  _______,  _______,  _______,  _______,
    ],
    [   #GAMING
        KC.GRV,   KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,                                            KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.DEL,
        KC.TAB,   KC.Z,     KC.Q,     KC.W,     KC.E,     KC.R,                                             KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,     KC.BSPC,
        KC.ESC,   KC.A,     KC.A,     KC.S,     KC.D,     KC.F,                                             KC.H,     KC.J,     KC.K,     KC.L,     KC.SCLN,  KC.QUOT,
        KC.LSFT,  KC.LCTL,  KC.X,     KC.C,     KC.V,     KC.B,                                             KC.N,     KC.M,     KC.COMM,  KC.DOT,   KC.SLSH,  KC.RSFT,
                            LOWER,    KC.LCTL,  KC.LALT,  KC.G,     KC.SPC,                       KC.ENT,   RAISE,    KC.RGUI,  KC.RALT,  KC.RCTL,
    ]

]
keyboard.debug_enabled = False

print("Free Memory: ", gc.mem_free())

#Show Keybaord is ready - console output only
print("Loaded")

if __name__ == '__main__':
    keyboard.go()

