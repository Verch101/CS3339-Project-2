from cstest import *
import sys
import os, os.path, stat

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
