class battery:
    def __init__(self):
        self.MAX_BATTERY = 100.0
        self.batter_level = 0.0
        self.continueSending = False

    def updateStorage(self, kiloWattsGenerated):
        self.batteryLevel += kiloWattsGenerated
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
        if(self.battery - 2.5 > self.MAX_BATTERY * 0.8):
            self.battery -= 4.0
        # check if after sending power if above the minimum threshold then continue
        # to use battery power
        elif(self.battery - 2.5 < self.MAX_BATTERY * 0.8 and self.battery - 2.5 > self.MAX_BATTERY * 0.25):
            self.battery -= 2.5
            self.continueSending = True
        elif(self.battery - 2.5 < self.MAX_BATTERY * 0.25):
            self.continueSending = False



