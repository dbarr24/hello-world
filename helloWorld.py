#!/usr/bin/env python

import sys
import serial
from array import array
	
ser = serial.Serial(
		
	port='/dev/ttyUSB0',
	#port='/dev/ttyAMA0',
	baudrate = 9600,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	timeout=1
	)

count = 0
data = []
while (count < 10):
	x = ser.readline()
	if x != "":
                data.append(x)
                count = count + 1
		print x

fh = open("BarcodeData.txt", "w")
fh.writelines(data)
fh.close()

#scp pi@172.20.10.5:BarcodeData.txt
