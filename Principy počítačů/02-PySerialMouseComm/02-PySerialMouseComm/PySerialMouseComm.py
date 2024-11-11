import serial
import time
import keyboard

print("Initializing RS-232 port ...")

serialPort = serial.Serial()
serialPort.baudrate = 1200
serialPort.bytesize = serial.SEVENBITS
serialPort.stopbits = serial.STOPBITS_ONE
serialPort.parity = serial.PARITY_NONE

#region Connect to correct RS-232 controller and initialize RS-232 port
serialPort.port = "COM3"

serialPort.timeout = 0.5

serialPort.open()

print("Initializing serial mouse ...")

#endregion
#region RS-232 mouse initialization

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

##############################################################################
# TO DO: Actual communication using Microsoft Serial Mouse with wheel protocol
# This will be implemented in the 3rd lecture ...
##############################################################################

# Wait for Ctrl key press before ending the program ...
print("Press and hold Ctrl key to end the program ...")
done = False
while not done:
    # If Ctrl key is pressed, then ...
    #region
    if keyboard.is_pressed('ctrl'):
        print("*** Ctrl key is now pressed, please release Ctrl key to end ***")
        while keyboard.is_pressed('ctrl'):
            pass
        #endregion
        done = True

# Stop communication with the RS-232 controller:
serialPort.close()