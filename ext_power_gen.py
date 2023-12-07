import SW

class ext_power_gen:
    def __init__(self):
        self.factor = 0.8

    def getSWValue(self):
        val = SW.read()
        result = val & 0b0000000011
        return result

    '''
    get the values for the current day's power generation
    '''
    def generatePower(self):
        swValue = self.getSWValue()
        if(swValue == 0):
            self.solar = 1.0 * self.factor
            self.wind = 1.0 * self.factor
        elif(swValue == 1):
            self.solar = 1.0 * self.factor
            self.wind = 3.0 * self.factor
        elif(swValue == 2):
            self.solar = 3.0 * self.factor
            self.wind = 1.0 * self.factor
        elif(swValue == 3):
            self.solar = 3.0 * self.factor
            self.wind = 3.0 * self.factor
        else:
            self.solar = 1.0 * self.factor
            self.wind = 1.0 * self.factor

        return self.solar, self.wind

