# handwired/floydm/liryo58

![handwired/floydm/liryo58](imgur.com image replace me!)

*A short description of the keyboard/project*

* Keyboard Maintainer: [Floyd Maloto](https://github.com/floydm)
* Hardware Supported: YD-RP2040, Pi Pico
* Hardware Availability: https://github.com/floydm/liryo58

Make example for this keyboard (after setting up your build environment):

    qmk compile -kb handwired/floydm/liryo58 -km default

Flashing example for this keyboard:

    qmk flash -kb handwired/floydm/liryo58 -km default -bl uf2-split-left

See the [build environment setup](https://docs.qmk.fm/#/getting_started_build_tools) and the [make instructions](https://docs.qmk.fm/#/getting_started_make_guide) for more information. Brand new to QMK? Start with our [Complete Newbs Guide](https://docs.qmk.fm/#/newbs).

## Bootloader

Enter the bootloader in 3 ways:

* **Bootmagic reset**: Hold down the key at (0,0) in the matrix (usually the top left key or Escape) and plug in the keyboard
* **Physical reset button**: Briefly press the button on the back of the PCB - some may have pads you must short instead
* **Keycode in layout**: Press the key mapped to `QK_BOOT` if it is available
