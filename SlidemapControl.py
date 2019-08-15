import serial
import time

class GrblComm:

    def __init__(self, port, baud, reponse, debug):
        #Initialize variables
        self.port = port
        self.baud = baud
        self.buffSize = 100
        self.response = response
        self.debug = debug

        #Connect to device running Grbl firmware
        if(self.debug):
            print("Connecting to Grbl")

        self.ser = serial.Serial(self.port, self.baud)
        time.sleep(1)

        if(self.debug):
            print("Grbl device connected")

    #Return the current baudrate
    def getBaud(self):
        if(self.debug):
            print("Baudrate is " + self.baud)
        return self.baud

    #Return the current USB port
    def getPort(self):
        if(self.debug):
            print("Baudrate is " + self.port)
        return self.port

    #Move device rapidly using G00 axis all move at max speed to position specified
    def rapidMovement(self,posStr):
        self.sendGCode('G00 ' + posStr)
        if(self.response):
            resp = ser.read(self.buffSize)
            if(self.debug):
                print(resp)

    #Move device in a line using G01 axis move at the proper speed so all stop movign at the same time
    def linearMovement(self,posStr):
        self.sendGCode('G01 ' + posStr)
        if(self.response):
            resp = ser.read(self.buffSize)
            if(self.debug):
                print(resp)

    #Inform Grbl G-Code commands will be sent in inches
    def useInches(self):
        self.sendGCode('G20')
        if(self.response):
            resp = ser.read(self.buffSize)
            if(self.debug):
                print(resp)

    #Inform Grbl G-Code commands will be sent in mm
    def useMM(self):
        self.sendGCode('G21')
        if(self.response):
            resp = ser.read(self.buffSize)
            if(self.debug):
                print(resp)

    #Move device to the set home position (Does not home device)
    def returnHome(self):
        self.sendGCode('G28')
        if(self.response):
            resp = ser.read(self.buffSize)
            if(self.debug):
                print(resp)

    #Send a G-Code command
    def sendGCode(self,cmd):
        if(self.debug):
            print(cmd)
        self.ser.write(str.encode(cmd + '\r\n'))

    #Disconnect from device running Grbl firmware
    def closeSer(self):
        if(self.debug):
            print("Disconnceting from Grbl")
        self.ser.close()
