import SW

class ext_power_gen:
    global solar
    global wind

    def getSWValue(self):
        SW.open_dev()
        val = SW.read()
        return val

    '''
    get the values for the current day's power generation
    '''
    def generatePower(self):
        swValue = self.getSWValue()
        if(swValue == 0):
            solar = 1.0
            wind = 1.0
        elif(swValue == 1):
            solar = 1.0
            wind = 3.0
        elif(swValue == 2):
            solar = 3.0
            wind = 1.0
        elif(swValue == 3):
            solar = 3.0
            wind = 3.0
        else:
            solar = 1.0
            wind = 1.0

        return solar, wind

