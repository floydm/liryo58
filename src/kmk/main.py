import board

from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.extensions.RGB import RGB

keyboard = KMKKeyboard()

layers = Layers()

split = Split(
    split_side=SplitSide.LEFT,
    split_flip=True,  # If both halves are the same, but flipped, set this True
    split_type=SplitType.UART,  # Defaults to UART
    uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
    data_pin=board.GP1,  # The primary data pin to talk to the secondary device with
    data_pin2=board.GP0,  # Second uart pin to allow 2 way communication
    use_pio=True,  # allows for UART to be used with PIO
)
rgb = RGB(pixel_pin=board.GP23, num_pixels=1)

XXXXXXX = KC.NO
_______ = KC.TRNS
LOWER = KC.MO(1)
RAISE = KC.MO(2)

keyboard.extensions = [rgb]
keyboard.modules = [layers, split]

keyboard.keymap = [
    [  # QWERTY
        # HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----#ENCODER--#ENCODER--# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----
        KC.GRV,   KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,                                            KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.BSPC,
        KC.TAB,   KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,                                             KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,     KC.MINS,
        KC.ESC,   KC.A,     KC.S,    KC.D,     KC.F,     KC.G,                                             KC.H,     KC.J,     KC.K,     KC.L,     KC.SCLN,  KC.QUOT,
        KC.LSFT,  KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,                                             KC.N,     KC.M,     KC.COMM,  KC.DOT,   KC.SLSH,  KC.RSFT,
                            KC.LGUI,  KC.LCTL,  KC.LALT,  LOWER,    KC.SPC,                       KC.ENT,   RAISE,    KC.RGUI,  KC.RALT,  KC.RCTL,
    ],
    [  #LOWER
        # HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----#ENCODER--#ENCODER--# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----
        XXXXXXX,  KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,                                            KC.F6,    KC.F7,    KC.F8,    KC.F9,    KC.F10,   KC.F11,
        KC.GRV,   KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,                                            KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.F12,
        XXXXXXX,  KC.EXLM,  KC.AT,    KC.HASH,  KC.DLR,   KC.PERC,                                          KC.CIRC,  KC.AMPR,  KC.ASTR,  KC.LPRN,  KC.RPRN,  KC.PIPE,
        XXXXXXX,  KC.EQL,   KC.MINS,  KC.PLUS,  KC.LCBR,  KC.RCBR,                                          KC.LBRC,  KC.RBRC,  KC.SCLN,  KC.COLN,  KC.BSLS,  XXXXXXX,
                            XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                      XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
    ],
    [  #RAISE
        # HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----#ENCODER--#ENCODER--# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                                          XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                                          KC.PGUP,  XXXXXXX,    KC.UP,  XXXXXXX,  XXXXXXX,  KC.BSPC,
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                                          KC.PGDN,  KC.LEFT,  KC.DOWN,  KC.RGHT,   KC.DEL,  KC.BSPC,
        XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                                          XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
                            XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                      XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
    ],
    [   #GAMING
        KC.GRV,   KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,                                            KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.DEL,
        KC.TAB,   KC.Z,     KC.Q,     KC.W,     KC.E,     KC.R,                                             KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,     KC.BSPC,
        KC.ESC,   KC.A,     KC.A,     KC.S,     KC.D,     KC.F,                                             KC.H,     KC.J,     KC.K,     KC.L,     KC.SCLN,  KC.QUOT,
        KC.LSFT,  KC.LCTL,  KC.X,     KC.C,     KC.V,     KC.B,                                             KC.N,     KC.M,     KC.COMM,  KC.DOT,   KC.SLSH,  KC.RSFT,
                            KC.LGUI,  KC.LCTL,  KC.LALT,  LOWER,    KC.SPC,                       KC.ENT,   RAISE,    KC.RGUI,  KC.RALT,  KC.RCTL,
    ]
]
#keyboard.debug_enabled = True

if __name__ == '__main__':
    keyboard.go()
