import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.GP10,
        board.GP11,
        board.GP12,
        board.GP13,
        board.GP14,
        board.GP15
    )
    row_pins = (
        board.GP5,
        board.GP6,
        board.GP7,
        board.GP8,
        board.GP9
    )
    diode_orientation = DiodeOrientation.COL2ROW
    coord_mapping = [
    0,  1,  2,  3,  4,  5,     35, 34, 33, 32, 31, 30,
    6,  7,  8,  9, 10, 11,     41, 40, 39, 38, 37, 36,
    12, 13, 14, 15, 16, 17,    47, 46, 45, 44, 43, 42,
    18, 19, 20, 21, 22, 23,    53, 52, 51, 50, 49, 48,
        25, 26, 27, 28, 29,    59, 58, 57, 56, 55
    ]

