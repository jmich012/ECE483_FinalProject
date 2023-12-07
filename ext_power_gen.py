import SW

class ext_power_gen:
    def __init__(self):
        self.factor = 0.8
        
    def generatePower(self):
        solarMax, windMax = self.getPowerValues()
        
        if(solarMax):
            self.solar = 1.5
        else:
            self.solar = 0.5
        
        if(windMax):
            self.wind = 1.5
        else:
            self.wind =  0.5

        return self.solar, self.wind
    






    def getSWValue(self):
        val = SW.read()
        result = val & 0b0000000011
        return result

    '''
    get the values for the current day's power generation
    '''
    def getPowerValues(self):
        swValue = self.getSWValue()
        solarMode = swValue & 0b0000000001
        windMode = swValue & 0b0000000010

        if(solarMode):
            solarMax = True
        else:
            solarMax = False
        
        if(windMode):
            windMax = True
        else:
            windMax = False

        return solarMax, windMax

