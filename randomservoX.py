import serial
import time
import random

arduinoData = serial.Serial('com11',9600)
#arduinoData = serial.Serial('/dev/',9600) for Rapberry 

# Let Arduino some time to reset
time.sleep(2)

global xposition
global xAngle


while True:

    global xposition
    low = 0; high = 180
    xposition = random.randint(low, high)
    time.sleep(1)
    #x = xposition


            
    #xAngle = xposition /1.3
    #arduinoData.write(str(xAngle).encode())

    def servoAngle (x) :
        global xAngle
        #print(x)
        xAngle = 180 - xposition /1.3
        print(xAngle)
        arduinoData.write(str(xAngle).encode())

               
       


    servoAngle(xposition)


    #ran_number must be populated by panServoAngle (x,y)  
    #ran_number = input("Enter number")
    #print(ran_number)
    #arduinoData.write(str(ran_number).encode())

time.sleep(1)
