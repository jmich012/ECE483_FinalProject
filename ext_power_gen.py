import SW

class ext_power_gen:
    def __init__(self):
        self.solar = 1
        self.wind = 1

    def getSWValue(self):
        val = SW.read()
        return val

    '''
    get the values for the current day's power generation
    '''
    def generatePower(self):
        swValue = self.getSWValue()
        if(swValue == 0):
            self.solar = 1.0
            self.wind = 1.0
        elif(swValue == 1):
            self.solar = 1.0
            self.wind = 3.0
        elif(swValue == 2):
            self.solar = 3.0
            self.wind = 1.0
        elif(swValue == 3):
            self.solar = 3.0
            self.wind = 3.0
        else:
            self.solar = 1.0
            self.wind = 1.0

        return self.solar, self.wind

