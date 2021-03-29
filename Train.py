from BlockClass import Block
import time

class TrainClass():
        def __init__(self,trainID):
                self.ID = trainID
                self.blocks = Block()

        authority = 0
        beacon = "Not In Service"
        speed_limit = 0
        commSpeed = 0
        velocityMPH = 0
        velocityKM = 0
        velocity = 0
        prevVel = 0.0001
        acceleration = 0
        accelerationDisplay = 0
        prevAcc = 0.0001
        deceleration = 0
        power = 0
        massTon = 40.9     #in tons
        mass = 0
        boarding = 0
        passenger = 20
        crew = 2
        temperature = 68
        doorStatus = False
        internalStatus = False
        externalStatus = False
        emergency = False
        service = False
        brakeFailure = False
        engineFailure = False
        signalFailure = False
        faults = 0
        blockNum = 0
        nextblock = 0
        line = "green"
        headlightCommand = False
        stationDoors = 0
        maxAcceleration = 0.5       #mps^2
        maxSpeed = 70            #km/hr
        minSpeed = 0
        prevPosition = 0
        currPos = 0

        #block grades and elevations
        blockGrade = 0
        elevation = 0
        cElevation = 0
        blockLength = 0
        switchBlock = 0
        signal = 0
        base = 0

        def calculateMass(self):
            self.massTon = 40.9 + (self.passenger+2)*(0.1068)
            self.mass = self.massTon * 907.185   #ton to kg conversion

        lastTime = 0.0
        timeChange = 0.0
        startTime = 0.0
        
        def calculateVelocity(self):

                #time since last calculation
                self.currTime = time.time()
                self.timeChange = self.currTime - self.startTime

                self.calculateMass()
        
                force = self.power / self.prevVel
                if (force != 0):
                        if (force>50):
                                force = 50
                        self.acceleration = force / self.mass

                        if self.emergency == 1:
                                self.acceleration = self.maxAcceleration
                        elif self.service == 1:
                                self.acceleration = self.maxAcceleration
                        elif (self.acceleration > self.maxAcceleration):
                                self.acceleration = self.maxAcceleration

                        self.velocity = self.prevVel + (self.timeChange/2)*(self.acceleration + self.prevAcc)

                        if self.velocity > self.kmhTOmps(self.maxSpeed):
                                self.velocity = self.kmhTOmps(self.maxSpeed)
                                self.acceleration = 0
                        
                        if self.velocity < self.minSpeed:
                                self.velocity = 0
                                self.acceleration = 0
                                self.brakesDone()

                        self.prevAcc = self.acceleration
                        self.prevVel = self.velocity

                #calculate position
                position = self.timeChange * self.velocity
                position -= self.currPos
                if (position > self.blockLength):
                        self.blocks.greenLine.pop(0)            #removes firt element
                        self.blockNum = self.blocks.greenLine[0]
                        self.currPos = position - self.blockLength 
                else:
                        self.currPos = self.blockLength - position


                if (self.velocity == 0):
                        self.prevVel = 0.0001
                if (self.acceleration == 0):
                        self.prevAcc = 0.0001
                self.startTime = self.currTime

                self.velocityMPH = self.mpsTOmph(self.velocity)
                self.velocityKM = self.mpsTOkm(self.velocity)
                return self.mpsTOmph(self.velocity)

        def mphTOmps(self,x):
                return x/2.23694

        def mpsTOmph(self,y):
                return y*2.23694

        def kmhTOmps(self,a):
                return a/3.6

        def mpsTOkm(self,b):
                return b*3.6


        def eBrakePressed(self):
                self.maxAcceleration = -2.73
                self.deceleration = 2.73
                self.accelerationDisplay = 0
                self.emergency = 1

        def serviceBrake(self):
                self.maxAcceleration = -1.2
                self.deceleration = 1.2
                self.accelerationDisplay = 0
                self.service = 1

        def brakesDone(self):
                self.maxAcceleration = 1.12
                self.emergency = 0
                self.service = 0
