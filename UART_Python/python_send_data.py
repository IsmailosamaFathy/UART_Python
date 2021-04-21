import serial, time
#initialization and open the port

#possible timeout values:
#    1. None: wait forever, block call
#    2. 0: non-blocking mode, return immediately
#    3. x, x is bigger than 0, float allowed, timeout block call

ser = serial.Serial()
#ser.port = "/dev/ttyUSB0"
ser.port = "com2"
#ser.port = "/dev/ttyS2"
ser.baudrate = 9600
ser.bytesize = serial.EIGHTBITS #number of bits per bytes
ser.parity = serial.PARITY_NONE #set parity check: no parity
ser.stopbits = serial.STOPBITS_ONE #number of stop bits
#ser.timeout = None          #block read
#ser.timeout = 1            #non-block read
ser.timeout = 2              #timeout block read
ser.xonxoff = False     #disable software flow control
ser.rtscts = False     #disable hardware (RTS/CTS) flow control
ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
ser.writeTimeout = 2     #timeout for write
ser.open()
count=1
avg=0
temp=0
#y[]
#print("sensor_Val: ",x)

while(1):
    x=ser.read(1)
    y=hex( int.from_bytes(x, 'big', signed=True) )
    z=int(y,16)
    print("sensor_Val:",z)
#problem of b'' "what is bytes objects in python" the name is Class method int.from_bytes  solved 
    #converted_num=int(x)
    temp=z+temp
    count=count+1 
    avg=temp/count
    print("AVG:",avg)


ser.close()    
    
