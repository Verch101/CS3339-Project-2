
postmem, postalu = '0', '0'
def write_back_unit(postmem, postalu, isempty ):
#cyclenum = '0'
#All of the register stuff. Going to have to think about this and come back to it. I need to use the Rd from the mips to write back to the registers array.

#assumming that that the postALUbuffer and POST-MEM are named that
#if postALUbuffer0 != x
	

#all of the out put stuff is here I dont know why.
 print '--------------------'
print 'Cycle:', cyclenum
print ' '
print 'Pre-Issue Buffer:'
print '        Entry 0:', preissuebuffer0
print '        Entry 1:', preissuebuffer1
print '        Entry 2:', preissuebuffer2
print '        Entry 3:', preissuebuffer3
print 'Pre_ALU Queue:'
print '        Entry 0:', preALUbuffer0
print '        Entry 1:', preALUbuffer1
print 'Post_ALU Queue:'
print '        Entry 0:', postALUbuffer0
print 'Pre_MEM Queue:'
print '        Entry 0:', preMEMbuffer0
print '        Entry 1:', preMEMbuffer1
print 'Post_MEM Queue:'
print '        Entry 0:', postMEMbuffer0
print ' '
print 'Registers'
print 'R00:', '        ', registers[0],'        ', registers[1],'        ', registers[2],'        ', registers[3],'        ', registers[4],'        ', registers[5],'        ', registers[6],'        ', registers[7]
print 'R08:', '        ', registers[8],'        ', registers[9],'        ', registers[10],'        ', registers[11],'        ', registers[12],'        ', registers[13],'        ', registers[14],'        ', registers[15]
print 'R16:', '        ', registers[16],'        ', registers[17],'        ', registers[18],'        ', registers[19],'        ', registers[20],'        ', registers[21],'        ', registers[22],'        ', registers[23]
print 'R24:', '        ', registers[24],'        ', registers[25],'        ', registers[26],'        ', registers[27],'        ', registers[28],'        ', registers[29],'        ', registers[30],'        ', registers[31]

#Cash stuff goes here But I dont understand that stuff yet, so this is just a black hole for right now. We can just put something in here later to make the diff closer.

print 'Data'
print '128:	4	16'
print '--------------------'

cyclenum = cyclenum + 1
def instruction_fetch():

def issue():

def MEM():


def ALU():

=======
from cstest.py import *
=======
from cstest import *
import sys
import os, os.path, stat

>>>>>>> 0c4f7af6b7313224a33af1196feafe9b1e62e5f3
PC = 96

if (len(sys.argv) > 1):
	bin_file, dis_file = sys.argv[1], sys.argv[2]
	print bin_file, dis_file
else:
 	print "Please enter valid input/output files"

infile = open(bin_file,'rb')



#returns the total number of lines in the file
def readLength():
	fileLength = os.stat(bin_file)[6]
	fileLength = fileLength/4	
	return fileLength

#returns a decimal value for each line in the binary file
def readFile():				
	#from struct import *
	#lenn = readLength()
	#byte = 0	
	byte = unpack('>I', infile.read(4))[0]
	#infile.read(1024)
	return byte


def instruction_fetch(bin_file):

	x = 0	
	while x<2:
		decimalValue = readFile()	
		line = convert_to_binary(decimalValue)
		#convert_to_binary(decimalValue)
		#convert_to_instruction(line,PC)
		#PC = PC + 4
		function = convert_to_instruction(line,PC)
		if (x == 0):
			IF_BIN_ONE = line
			IF_INST_ONE = function
		if (x == 1):
			IF_BIN_TWO = line
			IF_INST_TWO = function
#		output_cycle(registers, PC, function)
		x = x + 1
	print "two instructions were just loaded into the IF"
	print "they are", IF_INST_ONE, "and", IF_INST_TWO


instruction_fetch(bin_file)
PC = PC +4



#def pre_issue_buffer():


#def issue():

#def pre_mem_buffer():


#def pre_alu_buffer():


#def MEM():


#def ALU():


#def post_mem_buffer():


#def post_alu_buffer():
#def write_back_unit(postmem, postalu, isempty):
>>>>>>> 0a597c51d05f63b96ec93ea9c5d009233cb0f86d
