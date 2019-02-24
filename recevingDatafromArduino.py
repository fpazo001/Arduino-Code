import time
import serial
 
ser = serial.Serial('com11', 9600)

time.sleep(0.15)

i = 0
 
while True:
 #value = ser.readline()
 #value2 = ser.readline()
 #print(value)
 #time.sleep(0.5)


    msg = ser.readline()
    print (msg.decode('latin-1'))
    #decode = (msg.decode('latin-1'))
    DATASPLIT = msg.split(' , ')
    #i = i + 1
    time.sleep(0.5)


    pyDistance= DATASPLIT [0]
    pyMovement= DATASPLIT [1]
    

    print(pyDistance)
    print(pyMovement)


      
    
    
else:
    print ("Exiting")
exit()



