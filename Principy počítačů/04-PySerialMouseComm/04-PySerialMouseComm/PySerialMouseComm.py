import serial
import time
import keyboard
from numpy import *

print("Initializing RS-232 port ...")

serialPort = serial.Serial()
serialPort.baudrate = 1200
serialPort.bytesize = serial.SEVENBITS
serialPort.stopbits = serial.STOPBITS_ONE
serialPort.parity = serial.PARITY_NONE

#region RS-232 port and mouse initialization
serialPort.port = "COM5"

serialPort.timeout = 0.5

serialPort.open()

print("Initializing serial mouse ...")

# Make sure the mouse is powered down

serialPort.setRTS(False);
serialPort.setDTR(False);

time.sleep(0.150)
serialPort.flushInput();
serialPort.flushOutput();
time.sleep(0.150)

# Power up the mouse
serialPort.setDTR(True);
serialPort.setRTS(True);

# Read mouse identification data
# -> The identification data are not important to us, as we have single mouse type protocol hard-wired in our code,
#    so we read and throw ways everything mouse sends us at this time.
#    We expect the user not to move or click the mouse close to starting up the application, so the 0.5 second timeout
#    should be reasonable pause between initial mouse transmission of its identification data, and later data of actual
#    mouse move packets. 

done = False
while not done:
    data = serialPort.read(1024)
    if len(data) == 0:
        done = True
    else:
        print("Mouse identification data: ", data)
    
print("Serial mouse initialization completed ...")
#endregion

# Actual communication using Microsoft Serial Mouse with wheel protocol

####
#### VERSION 1: Decimal display of packet bytes ####
####
print()
print("V1: Decimal display: waiting for mouse packets (press and hold Ctrl key to continue to next example):")
done = False
pkt = []
while not done:
    # Read 4 byte packet from mouse into pkt list variable ...
    nextByte = serialPort.read(1)
    if len(nextByte) == 1:
        pkt.append(nextByte[0])
        if len(pkt) == 4:  # We got the whole 4 byte packet, start processing it ...

            print("Packet[", pkt[0], pkt[1], pkt[2], pkt[3], "] ", end="", flush=True)
            pkt = []

    # If Ctrl key is pressed, then ...
    #region
    if keyboard.is_pressed('ctrl'):
        print("*** Ctrl key is now pressed, please release Ctrl key to continue ***")
        while keyboard.is_pressed('ctrl'):
            pass
        #endregion
        done = True

####
#### VERSION 2: Hexadecimal display of packet bytes ####    
####
print()
print("V2: Hexadecimal display: waiting for mouse packets (press and hold Ctrl key to continue to next example):")
done = False
pkt = []
while not done:
    # Read 4 byte packet from mouse into pkt list variable ...
    nextByte = serialPort.read(1)
    if len(nextByte) == 1:
        pkt.append(nextByte[0])
        if len(pkt) == 4:  # We got the whole 4 byte packet, start processing it ...

            print("Packet[", format(pkt[0], "02X"), format(pkt[1], "02X"), format(pkt[2], "02X"), format(pkt[3], "02X"), "] ", end="", flush=True)
            pkt = []
    
    # If Ctrl key is pressed, then ...
    #region  
    if keyboard.is_pressed('ctrl'):
        print("*** Ctrl key is now pressed, please release Ctrl key to continue ***")
        while keyboard.is_pressed('ctrl'):
            pass
        #endregion
        done = True

####
#### VERSION 3: Getting info about pressed buttons ####    
####
print()
print("V3: Using bitwise ops to parse button state: waiting for mouse packets (press and hold Ctrl key to continue to next example):")
done = False
pkt = []
while not done:
    # Read 4 byte packet from mouse into pkt list variable ...
    nextByte = serialPort.read(1)
    if len(nextByte) == 1:
        pkt.append(nextByte[0])
        if len(pkt) == 4:  # We got the whole 4 byte packet, start processing it ...

            print("Packet[", format(pkt[0], "02X"), format(pkt[1], "02X"), format(pkt[2], "02X"), format(pkt[3], "02X"), "]=", end="")

            if pkt[0] & 0x20 != 0: 
                print("L", end="")
            else: 
                print("-", end="")

            if pkt[3] & 0x10 != 0: 
                print("M", end="")
            else: 
                print("-", end="")

            if pkt[0] & 0x10 != 0: 
                print("R", end="")
            else: 
                print("-", end="")

            print(end=" ", flush=True)
            pkt = []

    # If Ctrl key is pressed, then ...
    #region
    if keyboard.is_pressed('ctrl'):
        print("*** Ctrl key is now pressed, please release Ctrl key to continue ***")
        while keyboard.is_pressed('ctrl'):
            pass
        #endregion
        done = True

####
#### VERSION 4: Reading X and Y ####    
####
print()
print("V4: Reading X and Y: waiting for mouse packets (press and hold Ctrl key to continue to next example):")
done = False
pkt = []
while not done:
    # Read 4 byte packet from mouse into pkt list variable ...
    nextByte = serialPort.read(1)
    if len(nextByte) == 1:
        pkt.append(nextByte[0])
        if len(pkt) == 4:  # We got the whole 4 byte packet, start processing it ...

            print("Packet[", format(pkt[0], "02X"), format(pkt[1], "02X"), format(pkt[2], "02X"), format(pkt[3], "02X"), "]=", end="")

            if pkt[0] & 0x20 != 0: 
                print("L", end="")
            else: 
                print("-", end="")

            if pkt[3] & 0x10 != 0: 
                print("M", end="")
            else: 
                print("-", end="")

            if pkt[0] & 0x10 != 0: 
                print("R", end="")
            else: 
                print("-", end="")

            x = ((pkt[0] & 0x03) << 6) | (pkt[1] & 0x3F)
            print(", x=", x, end="")

            y = ((pkt[0] & 0x0C) << 4) | (pkt[2] & 0x3F)
            print(", y=", y, end="")

            print(end=" ", flush=True)
            pkt = []

    # If Ctrl key is pressed, then ...
    #region
    if keyboard.is_pressed('ctrl'):
        print("*** Ctrl key is now pressed, please release Ctrl key to continue ***")
        while keyboard.is_pressed('ctrl'):
            pass
        #endregion
        done = True

####
#### VERSION 5: Reading X and Y as signed integers ####    
####
print()
print("V5: Reading X and Y as signed integers: waiting for mouse packets (press and hold Ctrl key to continue to next example):")
done = False
pkt = []
while not done:
    # Read 4 byte packet from mouse into pkt list variable ...
    nextByte = serialPort.read(1)
    if len(nextByte) == 1:
        pkt.append(nextByte[0])
        if len(pkt) == 4:  # We got the whole 4 byte packet, start processing it ...

            print("Packet[", format(pkt[0], "02X"), format(pkt[1], "02X"), format(pkt[2], "02X"), format(pkt[3], "02X"), "]=", end="")

            if pkt[0] & 0x20 != 0: 
                print("L", end="")
            else: 
                print("-", end="")

            if pkt[3] & 0x10 != 0: 
                print("M", end="")
            else: 
                print("-", end="")

            if pkt[0] & 0x10 != 0: 
                print("R", end="")
            else: 
                print("-", end="")

            x = ((pkt[0] & 0x03) << 6) | (pkt[1] & 0x3F)
            x = int8(x)     # Reinterpret as 8-bit signed integer
            print(", x=", x, end="")

            y = ((pkt[0] & 0x0C) << 4) | (pkt[2] & 0x3F)
            y = int8(y)     # Reinterpret as 8-bit signed integer
            print(", y=", y, end="")

            print(end=" ", flush=True)
            pkt = []

    # If Ctrl key is pressed, then ...
    #region
    if keyboard.is_pressed('ctrl'):
        print("*** Ctrl key is now pressed, please release Ctrl key to continue ***")
        while keyboard.is_pressed('ctrl'):
            pass
        #endregion
        done = True

serialPort.close()