class battery:
    def __init__(self):
        self.MAX_BATTERY = 100.0
        self.batteryLevel = 0.0
        self.sending = False
        self.factor = 1
        self.upperThreshold = self.MAX_BATTERY * 0.8
        self.lowerThreshold = self.MAX_BATTERY * 0.25

    def updateStorage(self, kiloWattsGenerated, peak):
        
        # Set the depletion factor based on power demand
        self.setFactor(peak)

        # Increase the battery level by the power generated, set in main.py
        self.batteryLevel += kiloWattsGenerated

        # Determine if there is a surplus of battery storage and correct for MAX
        self.determineSurplus()
            
        # Determine if the battery should be sending power
        self.evalThreshold()
        
        # Consume power from the battery
        if(self.sending):
            self.sendPower()

        return self.batteryLevel, self.sending
    
    
    
    
    
    
    
    def setFactor(self, peak):
        if peak:
            self.factor = 2.5
        else:
            self.factor = 1
    
    def determineSurplus(self):
        if self.batteryLevel > self.MAX_BATTERY:
            self.batteryLevel = self.MAX_BATTERY
        else:
            pass
        
    
    def evalThreshold(self):
        if(self.batteryLevel > self.upperThreshold):
            self.sending = True
        elif(self.batteryLevel < self.lowerThreshold):
            self.sending = False
        else:
            pass
        
    
    # Draw power from the battery
    def sendPower(self):
        baseConsumption = 1.0
        consumption = baseConsumption * self.factor
        self.batteryLevel -= consumption


    



