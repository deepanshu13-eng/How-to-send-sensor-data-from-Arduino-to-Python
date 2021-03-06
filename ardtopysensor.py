import serial          # It is used for communication between Arduino and Python.
import time            # It is used to set some delay time in the program when required.


arduinoData = serial.Serial('com6',9600) # Setting arduino port to COM6 and serial rate at 9600 bits per second.
arduinoData.timeout = 1

time.sleep(2)                            # Making a delay for some seconds so that Python can recieve data from Arduino and there will be no error, if we will not give some delay time then Python will not be able to recieve full data and will show error.  

while True:                              # Starting while loop.

    data = arduinoData.readline().decode('ascii')                          # Reading data values and decoding data values coming from Arduino.
    valueSplit = data.split('x')                                           # Python will automatically split the data values when it will find any "x" in between. 
    
    Value1 = valueSplit[0]                                                 # Putting first data value equal to Value1.
    Value2 = valueSplit[1]                                                 # Putting second data value equal to Value2.
    Value3 = valueSplit[2]                                                 # Putting third data value equal to Value3.


    
    print("Temperature Value   : " + Value1 + " *C")                       # Now the first data value is of Temperature so we are printing Temperature value in its correct format.
   
    print("Humidity Value      : " + Value2 + " %")                        # Now the second value is of Humidity so we are printing Humidity value in its correct format. 
                         
    print("Soil Moisture Value : " + Value3 + " %")                        # Now the third value is of Soil Moisture so we are printing it its correct format

    print("---------------------------------------------------------------") 

    

arduinoData.close()  # Finally closing arduinoData.            

