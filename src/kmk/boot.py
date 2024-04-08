import board

from kmk.bootcfg import bootcfg

bootcfg(
    sense=board.GP10,  # column
    source=board.GP5, # row
    cdc_data=False,
    keyboard=True,
    midi=True,
    mouse=True,
    storage=True,
    usb_id=('floydm', 'Liryo58'),
)
