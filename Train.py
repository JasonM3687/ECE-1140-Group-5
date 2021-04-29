from BlockClass import Block
import time

class TrainClass():
        def __init__(self,trainID):
                self.ID = trainID
                self.blocks = Block()

        dispatched = False
        authority = 0
        beacon = "Not In Service"
        announcement = " "
        speed_limit = 0
        commSpeed = 0
        velocityMPH = 0
        velocityKM = 0
        velocity = 0
        set_speed = 0
        prevVel = 0.0001
        acceleration = 0
        prevAcc = 0.0001
        power = 0
        massTon = 40.9     #in tons
        mass = 0
        boarding = 0
        passenger = 0
        crew = 2
        temperature = 68
        doorStatus = False
        internalStatus = False
        externalStatus = False
        externalStatusTrack = False
        emergency = True
        emergencyPass = True
        emergencyFail = True
        service = True
        brakeFailure = False
        engineFailure = False
        signalFailure = False
        faults = 0
        prevblock=0
        blockNum = 0
        nextblock = 0
        line = 0
        headlightCommand = False
        stationDoors = 0
        maxAcceleration = 0       #mps^2
        maxSpeed = 70            #km/hr
        minSpeed = 0
        prevPosition = 0
        currPos = 0
        position=0

        wait = 0

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

                if (self.blocks.yard == True):
                        self.dispatched = False

                #do not calculate anything if true
                if (self.blocks.yard == True or self.dispatched == False):
                        self.acceleration = 0
                        self.velocity = 0
                        return
        
                force = self.power / self.prevVel
                if (force != 0 and self.blockNum != 0):
                        
                        self.acceleration = force / self.mass

                        if self.emergency == 1 or self.emergencyPass == 1 or self.emergencyFail == 1:
                                self.acceleration = self.maxAcceleration
                        elif self.service == 1:
                                self.acceleration = self.maxAcceleration
                        elif (self.acceleration > self.maxAcceleration):
                                self.acceleration = self.maxAcceleration

                        self.velocity = self.prevVel + (self.timeChange/2)*(self.acceleration + self.prevAcc)
                        #print(self.velocity)

                        #makes sure the velocity is never greater than the speed limit
                        if (self.velocity > self.mphTOmps(self.set_speed)) and (self.mphTOmps(self.set_speed) < self.mphTOmps(self.speed_limit)):
                                self.velocity = self.mphTOmps(self.set_speed)
                                self.acceleration = 0
                        elif (self.velocity > self.mphTOmps(self.speed_limit)):
                                self.velocity = self.speed_limit
                                self.acceleration = 0

                        #makes sure the velocity never exceeds the max speed
                        if self.velocity > self.kmhTOmps(self.maxSpeed):
                                self.velocity = self.kmhTOmps(self.maxSpeed)
                                self.acceleration = 0
                        
                        #if velocity becomes less than zero, it is essentially zero
                        if self.velocity < self.minSpeed and self.emergencyPass == 0 and self.emergencyFail == 0 and self.emergency == 0 and self.service == 0:
                                self.velocity = 0
                                self.acceleration = 0
                                self.brakesDone()
                        elif self.velocity < self.minSpeed:
                                self.velocity = 0
                                self.acceleration = 0

                        self.prevAcc = self.acceleration
                        self.prevVel = self.velocity

                #calculate position
                self.position += self.timeChange * self.velocity

                if self.blockNum == 0 and self.blocks.yard == False:
                        self.blocks.lineRoute.pop(0)
                        self.blockNum = self.blocks.lineRoute[0]
                        self.position=0
                elif (self.position > self.blockLength):
                        self.blocks.lineRoute.pop(0)            #removes firt element
                        self.blockNum = self.blocks.lineRoute[0]
                        self.currPos = self.position - self.blockLength
                        self.position=0
                else:
                        self.currPos = self.blockLength - self.position


                if (self.velocity == 0):
                        self.prevVel = 0.0001
                if (self.acceleration == 0):
                        self.prevAcc = 0.0001
                self.startTime = self.currTime

                self.velocityMPH = self.mpsTOmph(self.velocity)
                self.velocityKM = self.mpsTOkm(self.velocity)
                #print(self.currPos)
                return self.mpsTOmph(self.velocity)

        def mphTOmps(self,x):
                return x/2.23694

        def mpsTOmph(self,y):
                return y*2.23694

        def kmhTOmps(self,a):
                return a/3.6

        def mpsTOkm(self,b):
                return b*3.6

        def eBrakePressed(self,num):
                self.maxAcceleration = -2.73
                if num == 0:
                        self.emergencyPass = 1
                elif num == 1:
                        self.emergency = 1
                elif num == 2:
                        self.emergencyFail = 1

        def serviceBrake(self):
                self.maxAcceleration = -1.2
                self.service = 1

        def brakesDone(self):
                self.maxAcceleration = 0.5
                self.emergency = 0
                self.service = 0
                self.emergencyPass = 0
                self.emergencyFail = 0

        def openDoors(self):
                if (self.doorStatus == 0 and self.stationDoors != -1):
                        self.doorStatus = False
                elif(self.stationDoors!=-1 or self.doorStatus == 1):
                        self.doorStatus=True
                else:
                        self.doorStatus=False

        def calculatePassengers(self):
                if (self.boarding != 0 and self.prevblock!=self.blockNum):
                        temp = self.passenger
                        self.passenger = self.boarding - temp
                if self.passenger > 250:
                        self.passenger = 250
                self.prevblock=self.blockNum
                

        def setLine(self,line):
                if line == 0:
                        self.blocks.initialize("red")
                        self.blockNum = self.blocks.lineRoute[0]
                elif line == 1:
                        self.blocks.initialize("green")
                        self.blockNum = self.blocks.lineRoute[0]
                
        def switches(self):
                if self.line == 0:
                        self.blocks.redSwitchYard(self.base,self.switchBlock)
                        
                elif self.line == 1:
                        self.blocks.greenSwitchYard(self.base,self.switchBlock)
                        self.blockNum = self.blocks.lineRoute[0]
