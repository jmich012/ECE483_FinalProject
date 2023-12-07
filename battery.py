class battery:
    def __init__(self):
        self.MAX_BATTERY = 100.0
        self.batteryLevel = 0.0
        self.continueSending = False
        self.factor = 1

    def updateStorage(self, kiloWattsGenerated, peak):
        if peak:
            self.factor = 2
        else:
            self.factor = 1
            
        self.batteryLevel += kiloWattsGenerated

        if self.batteryLevel > self.MAX_BATTERY:
            self.batteryLevel = self.MAX_BATTERY
            return self.batteryLevel, self.continueSending 

        if(self.batteryLevel > self.MAX_BATTERY * 0.8):
            self.sendPower()
        elif(self.continueSending):
            self.sendPower()
        elif(self.batteryLevel < self.MAX_BATTERY * 0.25):
            self.continueSending = False

        return self.batteryLevel, self.continueSending


    def sendPower(self):
        # if after sending power to the building and the remaing battery level is
        # above 80% then sell power
        if(self.batteryLevel - 2.5 > self.MAX_BATTERY * 0.8):
            self.batteryLevel -= 4.0 * self.factor
        # check if after sending power if above the minimum threshold then continue
        # to use battery power
        elif(self.batteryLevel - 2.5 < self.MAX_BATTERY * 0.8 and self.batteryLevel - 2.5 > self.MAX_BATTERY * 0.25):
            self.batteryLevel -= 2.5 * self.factor
            self.continueSending = True
        elif(self.batteryLevel - 2.5 < self.MAX_BATTERY * 0.25):
            self.continueSending = False



