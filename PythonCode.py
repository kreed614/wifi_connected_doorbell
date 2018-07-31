#Import required libraries
import serial
import requests

#connect to aruduino through serial
ser = serial.Serial('/dev/ttyACM0', 9600)

#flush all previous input
ser.flushInput()

while True:
    try:
        #read data from arduino
        lineBytes = ser.readline()
        
        #convert to string
        line = lineBytes.decode('utf-8')
        
        #checks for signal from button
        if line.startswith("HIGH"):
            
            #sends HTTP post to IFTTT
            r = requests.post('https://maker.ifttt.com/trigger/{SendText}/with/key/dpjUghCYLS99tia8lyM_dm', data = {'key':'value'})

            #shows the IFTTT respose
            print(r.text)

        else:
            print('...')

    #stops the while loop
    except KeyboardInterrupt:
        break
