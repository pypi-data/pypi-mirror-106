# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2021 James Carr
#
# SPDX-License-Identifier: Unlicense


# An example to read the configuration, polarity inversion and state of all
# 16 inputs from the TCA9555.


import board

from community_tca9555 import TCA9555


# Create the TCA9555 expander using the board default I2C
expander = TCA9555(board.I2C())

# Read the configuration of all 16 pins
# 0 = output, 1 = input
in_or_out = expander.configuration_ports
print("Configuration\n{:016b}".format(in_or_out))

# Read the polarity inversion state of all 16 pins
polarity_inversion = expander.polarity_inversions
print("Polarity inversion\n{:016b}".format(polarity_inversion))

# Read the input state of all 16 pins
input_state = expander.input_ports
print("Input state\n{:016b}".format(input_state))

# Read the output state of all 16 pins
# At power up, this defaults to 1111111111111111
output_state = expander.output_ports
print("Output state\n{:016b}".format(output_state))
