from roboclaw import Roboclaw

rc = Roboclaw("/dev/ttyACM0",115200)

rc.Open()

address = 0x80

class Mode():
	RC = 0
	ANALOG = 1
	SIMPLESERIAL = 2
	PACKETSERIAL = 3

#Get version string
write = rc.SetConfig(address, Mode.PACKETSERIAL)
if write==False:
	print "Can't write"

response = rc.GetConfig(address)
if response[0]==False:
	print "Can't read"
else:
	print repr(response[1])

