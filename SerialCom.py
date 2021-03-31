import serial

ser = serial.Serial('COM3', baudrate = 9600, timeout = 1)
limit = 150
while 1:

    arduinoData = ser.readline().decode('ascii')
    power = arduinoData
    print("Power" + power)
    arduinoData = ser.readline().decode('ascii')
    headlights = arduinoData
    print("headlights" + headlights)
    arduinoData = ser.readline().decode('ascii')
    internallights = arduinoData
    print("internallights" + internallights)
    arduinoData = ser.readline().decode('ascii')
    servicebrake = arduinoData
    print("servicebrake" + servicebrake)
    arduinoData = ser.readline().decode('ascii')
    emergencybrake = arduinoData
    print("emergencybrake" + emergencybrake)
    arduinoData = ser.readline().decode('ascii')
    doors = arduinoData
    print("doors" + doors)
    ser.write(limit)
    arduinoData = ser.readline().decode('ascii')
    print(arduinoData)
   
