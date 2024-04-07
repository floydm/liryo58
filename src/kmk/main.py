print("Starting Liryo58 v1")

import board
import gc

from kb import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

# import modules
from kmk.modules.layers import Layers as _Layers
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.modules.combos import Combos, Chord, Sequence
from kmk.modules.holdtap import HoldTap
from kmk.modules.tapdance import TapDance

# import extensions
from kmk.extensions.rgb import RGB

keyboard = KMKKeyboard()

split = Split(
    split_flip=True,  # If both halves are the same, but flipped, set this True
    split_type=SplitType.UART,  # Defaults to UART
    uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
    data_pin=board.GP1,  # The primary data pin to talk to the secondary device with
    data_pin2=board.GP0,  # Second uart pin to allow 2 way communication
    use_pio=False,  # allows for UART to be used with PIO
)

# RGB Layer Stuff
val = 5

rgb = RGB(
    pixel_pin=board.GP23,
    num_pixels=1,
    hue_default=0,              # in range 0-255: 0/255-red, 85-green, 170-blue
    sat_default=0,
    val_default=0,
)

class Layers(_Layers):
    last_top_layer = 0

    def after_hid_send(self, keyboard):
        if keyboard.active_layers[0] != self.last_top_layer:
            self.last_top_layer = keyboard.active_layers[0]
            if self.last_top_layer == 0:  # default
                rgb.set_hsv_fill(0, 0, 0)
                print('Default Layer')
            elif self.last_top_layer == 1:
                rgb.set_hsv_fill(0, 0, val) # white
                print('Lower Layer')
            elif self.last_top_layer == 2:
                rgb.set_hsv_fill(0, 255, val)  # red
                print('Raise Layer')
            elif self.last_top_layer == 3:
                rgb.set_hsv_fill(120, 255, val)     # blue
                print('Gaming Layer')
            elif self.last_top_layer == 4:
                rgb.set_hsv_fill(70, 255, val)     # green
                print('Function Layer')
            rgb.show()

layers = Layers()
combos = Combos()
holdtap = HoldTap()
tapdance = TapDance()

# Append extensions and modules
keyboard.extensions = [rgb]
keyboard.modules = [layers, split, combos, holdtap, tapdance]

# Key Stuff
XXXXXXX = KC.NO
_______ = KC.TRNS
LOWER = KC.MO(1)
RAISE = KC.MO(2)
FUNCTION_LYR = KC.MO(4)

# Combos
combos.combos = [
    Sequence((KC.ESC, KC.N1), KC.TG(3)),     # Toggle Layer 3 (Gaming)
]

# Tap Dances
FUNCTION_TD = KC.TD(
    LOWER,
    FUNCTION_LYR,
    KC.TG(3),
)

keyboard.keymap = [
    [  # 0 - QWERTY
        # HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----#ENCODER--#ENCODER--# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----
        KC.GRV,   KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,                                            KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.BSPC,
        KC.TAB,   KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,                                             KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,     KC.MINS,
        KC.ESC,   KC.A,     KC.S,     KC.D,     KC.F,     KC.G,                                             KC.H,     KC.J,     KC.K,     KC.L,     KC.SCLN,  KC.QUOT,
        KC.LSFT,  KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,                                             KC.N,     KC.M,     KC.COMM,  KC.DOT,   KC.SLSH,  KC.RSFT,
                            KC.LCTL,  KC.LALT,  KC.LGUI,  FUNCTION_TD,    KC.SPC,                 KC.ENT,   RAISE,    KC.RGUI,  KC.RALT,  KC.RCTL,
    ],
    [  # 1 - LOWER
        # HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----#ENCODER--#ENCODER--# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----
        XXXXXXX,  KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,                                            KC.F6,    KC.F7,    KC.F8,    KC.F9,    KC.F10,   KC.F11,
        KC.GRV,   KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,                                            KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.F12,
        XXXXXXX,  KC.EXLM,  KC.AT,    KC.HASH,  KC.DLR,   KC.PERC,                                          KC.CIRC,  KC.AMPR,  KC.ASTR,  KC.LPRN,  KC.RPRN,  KC.PIPE,
        XXXXXXX,  KC.EQL,   KC.MINS,  KC.PLUS,  KC.LCBR,  KC.RCBR,                                          KC.LBRC,  KC.RBRC,  KC.SCLN,  KC.COLN,  KC.BSLS,  KC.PSCR,
                            _______,  _______,  _______,  _______,  _______,                      _______,  _______,  _______,  _______,  _______,
    ],
    [  # 2 - RAISE - Navigation
        # HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----#ENCODER--#ENCODER--# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----
        KC.NLCK,  XXXXXXX,  XXXXXXX,  XXXXXXX,  KC.PSLS,  KC.PAST,                                          XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  KC.DEL,
        KC.TAB,   XXXXXXX,  KC.KP_7,  KC.KP_8,  KC.KP_9,  KC.PMNS,                                          KC.PGUP,  KC.HOME,    KC.UP,   KC.END,  XXXXXXX,  KC.BSPC,
        KC.ESC,   XXXXXXX,  KC.KP_4,  KC.KP_5,  KC.KP_6,  KC.PPLS,                                          KC.PGDN,  KC.LEFT,  KC.DOWN,  KC.RGHT,   KC.DEL,  KC.BSPC,
        XXXXXXX,  KC.KP_0,  KC.KP_1,  KC.KP_2,  KC.KP_3,  KC.PDOT,                                          XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  KC.PSCR,
                            _______,  _______,  _______,  _______,  _______,                      _______,  _______,  _______,  _______,  _______,
    ],
    [   # 3 - GAMING
        KC.GRV,   KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,                                            XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
        KC.T,     KC.N6,    KC.Q,     KC.W,     KC.E,     KC.R,                                             XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
        KC.ESC,   KC.LSFT,  KC.A,     KC.S,     KC.D,     KC.F,                                             XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
        KC.B,     KC.LCTL,  KC.Z,     KC.X,     KC.C,     KC.V,                                             XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
                            FUNCTION_TD,    KC.TAB,   KC.LALT,  KC.G,     KC.SPC,                 KC.ENT,   RAISE,    XXXXXXX,  XXXXXXX,  XXXXXXX,
    ],
    [  # 4 - Functions
        # HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----#ENCODER--#ENCODER--# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----
        KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,    KC.F6,                                            XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
        KC.F7,    KC.F8,    KC.F9,    KC.F10,   KC.F11,   KC.F12,                                           XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
        KC.F13,   KC.F14,   KC.F15,   KC.F16,   KC.F17,   KC.F18,                                           XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
        KC.F19,   KC.F20,   KC.F21,   KC.F22,   KC.F23,   KC.F24,                                           XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
                            _______,  _______,  _______,  _______,  _______,                      _______,  _______,  _______,  _______,  _______,
    ],
    [  # 5 -
        # HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----#ENCODER--#ENCODER--# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                                          XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                                          XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                                          XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                                          XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
                            _______,  _______,  _______,  _______,  _______,                      _______,  _______,  _______,  _______,  _______,
    ],
    [  # 6 -
        # HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----#ENCODER--#ENCODER--# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                                          XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                                          XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                                          XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                                          XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
                            _______,  _______,  _______,  _______,  _______,                      _______,  _______,  _______,  _______,  _______,
    ],
    [  # 7 -
        # HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----#ENCODER--#ENCODER--# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                                          XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                                          XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                                          XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                                          XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
                            _______,  _______,  _______,  _______,  _______,                      _______,  _______,  _______,  _______,  _______,
    ]
]
keyboard.debug_enabled = False

print("Free Memory: ", gc.mem_free())

#Show Keybaord is ready - console output only
print("Loaded")

if __name__ == '__main__':
    keyboard.go()

