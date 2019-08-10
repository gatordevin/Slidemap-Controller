import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 115200)
time.sleep(1)

ser.write(b'M17\r\n')
ser.write(b'M92 Y400\r\n')

#while True:
#    print("Please Enter Command:")
#    command = input()
#    if(command == "exit"):
#        break
#
#    gcode = command + '\r\n'
#    ser.write(str.encode(gcode))
pos = 0
while True:
    pos += 8
    gcode = "G0 Y" + str(pos) + '\r\n'
    print(gcode)
    ser.write(str.encode(gcode))
    time.sleep(2)

ser.write(b'M18\r\n')

time.sleep(0.5)
ser.close()
