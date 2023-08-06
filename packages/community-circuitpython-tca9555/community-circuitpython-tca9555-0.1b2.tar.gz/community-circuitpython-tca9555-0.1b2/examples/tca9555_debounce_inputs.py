# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2021 James Carr
#
# SPDX-License-Identifier: Unlicense


# A simple test to read the 16 inputs from the TCA9555.
# It uses the Debouncer library to print out when an input has changed.


import time
import sys
import board

from community_tca9555 import TCA9555

try:
    from adafruit_debouncer import Debouncer
except ImportError:
    # Make sure the Debounce library is available
    # It is a requirement of this example but not the library.
    print("Please install the Debounce library:")
    print("  To install to your Python environment")
    print("    pip3 install adafruit-circuitpython-debouncer")
    print("  To install direct to a connected CircuitPython device")
    print("    circup install adafruit-circuitpython-debouncer")
    sys.exit()


# Create the TCA9555 expander using the board default I2C
expander = TCA9555(board.I2C())


# Prepare to read the 16 inputs
# Create a tuple of buttons which are debounced so they can be monitored for changes.
# This reads the bits from the expander individually, instead of as bytes or a word.
# This is to make the debouncing easier.
buttons = (
    Debouncer(lambda: expander.input_port_0_pin_0),
    Debouncer(lambda: expander.input_port_0_pin_1),
    Debouncer(lambda: expander.input_port_0_pin_2),
    Debouncer(lambda: expander.input_port_0_pin_3),
    Debouncer(lambda: expander.input_port_0_pin_4),
    Debouncer(lambda: expander.input_port_0_pin_5),
    Debouncer(lambda: expander.input_port_0_pin_6),
    Debouncer(lambda: expander.input_port_0_pin_7),
    Debouncer(lambda: expander.input_port_1_pin_0),
    Debouncer(lambda: expander.input_port_1_pin_1),
    Debouncer(lambda: expander.input_port_1_pin_2),
    Debouncer(lambda: expander.input_port_1_pin_3),
    Debouncer(lambda: expander.input_port_1_pin_4),
    Debouncer(lambda: expander.input_port_1_pin_5),
    Debouncer(lambda: expander.input_port_1_pin_6),
    Debouncer(lambda: expander.input_port_1_pin_7),
)


# Loop forever
while True:
    time.sleep(0.001)
    for index, button in enumerate(buttons):
        button.update()  # Update the debounce information
        if button.rose:
            print("Button", index, "rose")
        if button.fell:
            print("Button", index, "fell")
