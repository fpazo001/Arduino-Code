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
    low = 0; high = 300
    xposition = random.randint(low, high)
    time.sleep(1)
    
   
    xAngle = xposition /1.3
    arduinoData.write(str(xAngle).encode())





    #ran_number must be populated by panServoAngle (x,y)  
    #ran_number = input("Enter number")
    #print(ran_number)
    #arduinoData.write(str(ran_number).encode())

time.sleep(1)
