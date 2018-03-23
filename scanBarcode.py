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
while (count < 5):
	x = ser.readline()
	if x != "":
		x = "Barcode " + str(count + 1) + ": " + x
                data.append(x)
                count = count + 1
		print x

fh = open("BarcodeData.txt", "w")
fh.writelines(data)
fh.close()
