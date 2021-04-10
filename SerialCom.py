import serial

def getDoors():
    return doors

def getSpeed():
    return speed

def getHeadlights():
    return headlights

def getInternallights():
    return internallights

def getServiceBrake():
    return servicebrake

def getEmergencyBrake():
    return emergencybrake


if __name__ == "__main__":

    ser = serial.Serial('COM3', baudrate = 9600, timeout = 1)

    while 1:

    
        arduinoData = ser.readline().decode('ascii')
        doors = arduinoData
        print("Doors: " + doors)
        arduinoData = ser.readline().decode('ascii')
        speed = arduinoData
        print("Speed: " + speed)
        arduinoData = ser.readline().decode('ascii')
        headlights = arduinoData
        print("Headlights: " + headlights)
        arduinoData = ser.readline().decode('ascii')
        internallights = arduinoData
        print("Internallights: " + internallights)
        arduinoData = ser.readline().decode('ascii')
        servicebrake = arduinoData
        print("Servicebrake: " + servicebrake)
        arduinoData = ser.readline().decode('ascii')
        emergencybrake = arduinoData
        print("Emergencybrake: " + emergencybrake)
  
    

   
