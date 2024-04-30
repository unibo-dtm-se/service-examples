class Light:
    
    def __init__(self, identifier):
        self.id = identifier
        self.state = "off"
        self.log("created.")

    def isOn(self):
        if self.state == "on":
            return True
        else:    
            return False

    def getState(self):
        return self.state
    
    def getLightId(self):
        return self.id
    
    def turnOn(self):
        self.state = "on"
        self.log("turned on")

    def turnOff(self):
        self.state = "off"
        self.log("turned off")

    def log(self, msg):
        print("[Light %s] %s" % (self.id, msg))


class LightSwitch:

    def __init__(self, id, lightToConnect):
        self.id = id
        self.connectedLight = lightToConnect
    
    def press(self):
        self.log("pressed")
        if self.connectedLight.isOn():
            self.connectedLight.turnOff()
        else: 
            self.connectedLight.turnOn()

    def connectTo(self, light):
        self.connectedLight = light

    def log(self, msg):
        print("[LightSwitch %s] %s" % (self.id, msg))


class SmartRoom:

    def __init__(self, id):
        self.id = id
        self.lights = {}
        self.lights["light-01"] = Light("light-01")
        self.lights["light-02"] = Light("light-02")
        self.lightSwitches = {}
        self.lightSwitches["switch-01"] = LightSwitch("switch-01", self.lights["light-01"])
        self.log("configured! Number of lights: %d Number of switches: %d" % (len(self.lights), len(self.lightSwitches)))

    def turnOn(self, lightId):
        if lightId in self.lights: 
            l = self.lights[lightId]
            l.turnOn()
        else:
            raise Exception("Light not existing")

    def getLightState(self, lightId):
        if lightId in self.lights: 
            l = self.lights[lightId]
            return l.getState()
        else:
            raise Exception("Light not existing")

    def press(self, switchId):
        if switchId in self.lightSwitches:
            s = self.lightSwitches[switchId]
            s.press()
        else:   
            raise Exception("Switch not found")    

    def addNewLight(self, newLight):
        lightId = newLight.getLightId()
        self.lights[lightId] = newLight
        self.log("new light added: %s" % lightId)

    def getCurrentLights(self):
        return self.lights.keys()

    def getCurrentLightSwitches(self):
        return self.lightSwitches.keys()

    def lock(self):
        self.log("locking the room...")    
        for light in self.lights.values():
            light.turnOff()

    def log(self, msg):
        print("[SmartRoom %s] %s" % (self.id, msg))



        


