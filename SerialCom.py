import serial
import time

#Methods to pass inputs values to Train Controller
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

#Main function used to grab arduino serial data
def main():
    #Open serial port communication on com3 with a baud rate of 2000000
    ser = serial.Serial('COM3', baudrate = 2000000, timeout = 1)
    
    while 1:
        
        #Read/store/print all data from arduino serial monitor 
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

#Run main function
if __name__ == "__main__":
    main()
    

        
    

   
