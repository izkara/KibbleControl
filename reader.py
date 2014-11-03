import serial
import time

STATUS_OK = "01"
RFID = serial.Serial('/dev/ttyAMA0', 115200, timeout=2)
while True:
    # time.sleep(1)
    if (RFID.isOpen() == False):
      RFID.open()

    else:
        RFID.write('\x18\x03\x00')
        print "inwaiting: " , RFID.inWaiting(100)

        try:
            fromReader = RFID.read()
            # fromReader += RFID.read(RFID.inWaiting())
            print "fromReader ASCII: ", fromReader
            print "fromReader HEX: ", fromReader.encode('hex')
        except Exception, e:
            print "DIDNT READ FROM RFID", e
            continue
        
        

        # time.sleep(3)
        # RFID.write('\x18\x03\x00')
        # if (RFID.inWaiting > 0):
        # fromReader = RFID.read(RFID.inWaiting())
        # print RFID.inWaiting()
        # print fromReader
        # print fromReader.encode('hex')
        # time.sleep(3)
        # RFID.write('\x43\x03\x01\xCD')
        # # if (RFID.inWaiting > 0):
        # fromReader = RFID.read(RFID.inWaiting())
        # print RFID.inWaiting()
        # print fromReader
        # print fromReader.encode('hex')
        # time.sleep(3)
        # RFID.write('\x18\x03\x00')
        # # if (RFID.inWaiting > 0):
        # fromReader = RFID.read(RFID.inWaiting())
        # print RFID.inWaiting()
        # print fromReader
        # print fromReader.encode('hex')


        # if (RFID.inWaiting > 0):
        #     fromReader = RFID.read()
        #     #if fromReader.encode('hex') == STATUS_OK :
        #     print fromReader
        #     print fromReader.encode('hex')
        # else: 
        #     RFID.flushInput()
        # RFID.write('\x43\x03\x01\xCD')
        # if (RFID.inWaiting() > 0):
        #     fromReader = RFID.read(100)
        #     #if fromReader.encode('hex') == STATUS_OK :
        #     print fromReader
        #     print fromReader.encode('hex')
        # else: 
        #     RFID.flushInput()
        # RFID.write('\x18\x03\x00')
        # if (RFID.inWaiting() > 0):
        #     fromReader = RFID.read(100)
        #     #if fromReader.encode('hex') == STATUS_OK :
        #     print fromReader
        #     print fromReader.encode('hex')
        # else: 
        #     RFID.flushInput()
        
    # print fromReader