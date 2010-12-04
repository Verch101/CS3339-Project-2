from struct import *
import os, os.path, stat


# Trying to read the first bit of each line to see what to excitute
add, j, JR, BEQ, addi  ='00000', '00010', '01000', '00100', '01000'
PC = 96
infile = open("test1.bin",'rb')


def readLength():
	fileLength = os.stat('test1.bin')[6]
	fileLength = fileLength/4	
	return fileLength

def readFile():
	#from struct import *
	#lenn = readLength()
	#byte = 0
	for 
		byte = [unpack('>I', infile.read(4))[0]]
	#infile.read(1024)
	return byte
	

print readFile()
	

while 1:
	line = infile.read(4)
	#line = unpack('>I', infile.read(4))[0]
	if not line:
	 break
	if line[0] == '0':
	 print line[0], line[1:6], line[7:12], line[13:18], line[19:24], line[25:31], ' ', PC, 'Invalid Instruction'
	 print >>f, line[0], line[1:6], line[7:12], line[13:18], line[19:24], line[25:31], line[32:36], PC, 'Invalid Instruction'
	if line[0] == '1':
	 print line[0], line[1:6], line[7:12], line[13:18], line[19:24], line[25:31], line[32:36], PC
	 if line[1:6] == add:
	  print 'add'
	 if line[1:6] == j:
	  print 'j'
	 if line[1:6] == JR:
	  print 'JR'
	 if line[1:6] == BEQ:
	  print 'BEQ'
	 if line[1:6] == addi:
	  print 'AADI'
	 print line
	PC = PC+4
