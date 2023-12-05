from ext_power_gen import ext_power_gen
from battery import battery
import LCD
import LEDR

powerGen = ext_power_gen()
bat = battery()

useGeneratedPower = False

led = LEDR.open_dev()
lcd = LCD.open_dev()

def updateDisplay():
    pass

while 1:
    # get the current values of the solar panels and wind turbine
    solar, wind = powerGen.generatePower()
    totalGeneratedPower = solar + wind

    # update the battery storage
    batteryLevel, useGeneratedPower = bat.updateStorage(totalGeneratedPower)

