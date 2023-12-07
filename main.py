#!/usr/bin/env python
from ext_power_gen import ext_power_gen
from battery import battery
import LCD
import LEDR
import KEY

powerGen = ext_power_gen()
bat = battery()

useGeneratedPower = False

LEDR.open_dev()
LCD.open_dev()
KEY.open_dev()

"""
needed for the writing to the LCD screen
"""
screen_x, screen_y, char_x,char_y = LCD.read()
LCD.erase()
LCD.clear()



def updateDisplay(solar, wind, batteryLevel, useGeneratedPower, peak):
    # build the battery percentage msg
    msg = "Battery: " + str(batteryLevel)
    LCD.text(0, char_y -1, msg)

    # msg for if grid power is being used
    if(useGeneratedPower):
        msg = "Grid Power: N"
    else:
        msg = "Grid Power: Y"

    LCD.text(0,char_y - 2, msg)

    # msg for if battery power is being used
    if(useGeneratedPower):
        msg = "Battery Power: Y"
    else:
        msg = "Battery Power: N"

    LCD.text(0,char_y - 3, msg)


    # msg for peak power usage
    if(peak):
        msg = "Peak Usage: Y"
    else:
        msg = "Peak Usage: N"

    LCD.text(0,char_y - 4, msg)

    # msg for high or low wind gen
    msg = "Wind: MIN"
    if(wind == 3.0):
        msg = "Wind: MAX"

    LCD.text(0,char_y - 5, msg)

    # msg for high or low solar gen
    msg = "Solar: MIN"
    if(solar == 3.0):
        msg = "Solar: MAX"

    LCD.text(0,char_y - 6, msg)

    LCD.show()



while 1:
    peak = KEY.read()
    print(peak)
    # get the current values of the solar panels and wind turbine
    solar, wind = powerGen.generatePower()
    totalGeneratedPower = solar + wind

    # update the battery storage
    batteryLevel, useGeneratedPower = bat.updateStorage(totalGeneratedPower, False)

    updateDisplay(solar,wind,batteryLevel, useGeneratedPower, False)
