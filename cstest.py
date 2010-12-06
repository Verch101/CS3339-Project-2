from struct import *
import os, os.path, stat


# Trying to read the first bit of each line to see what to excitute
add, j, JR, BEQ, addi  ='00000', '00010', '01000', '00100', '01000'
PC = 96
registers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
a = -1
#infile = open(bin_file,'rb')


#returns the total number of lines in the file
#def readLength():
#	fileLength = os.stat(bin_file)[6]
#	fileLength = fileLength/4	
#	return fileLength

#returns a decimal value for each line in the binary file
#def readFile():				
	#from struct import *
	#lenn = readLength()
	#byte = 0	
#	byte = unpack('>I', infile.read(4))[0]
	#infile.read(1024)
#	return byte
	


#converts above decimal value into binary so that
#we can break it up into code sections
def convert_to_binary(int):

    const = 0x80000000
    
    output = ""
    for i in range(1,33):
        if( int & const ):
            output = output + "1"
        else:
            output = output + "0"
        const = const >> 1
    return output



# here we define all the instructions that use 00000
# there are multiple ones with 00000 as a code
# so for those we need the 'SPECIAL' function codes
# these are the last six bits (ones w/o '00000' use those 6 for #other things..)
# 
def specOpCode(special):
	ADD, SLL, SRL, AND, OR, MOVZ, NOP, BREAK, SUB  = '100000', '000000', '000010', '100100', '100101', '001010', '000000', '001101', '100010'
	if special == ADD:
		return 'ADD'
	if special == SLL:
		return 'SLL'
	if special == SRL:
		return 'SRL'
	if special == AND:
		return 'AND'
	if special == OR:
		return 'OR'
	if special == MOVZ:
		return 'MOVZ'
	if special == NOP:
		return 'NOP'
	if special == BREAK:
		return 'BREAK'
	if special == SUB:
		return 'SUB'


# this is to convert the last 11 bits of LW and SW functions
# into decimal so we see what adress they point to
def convert_imm_address(line):
	bits = 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1
	# 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024
	#1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1
	i = 0
	address = 0
	while i < 11:
		if line[i] == '1':	
			address = address + bits[i]
		i = i + 1
		#print i
	return address

def convert_r(line):
	bits = 16, 8, 4, 2, 1
	# 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024
	#1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1
	i = 0
	r = 0
	while i < 5:
		if line[i] == '1':	
			r = r + bits[i]
		i = i + 1
		#print i
	return r
	

#um....i forgot what this does
#oh, this lets the 'MAIN' program know that
# we do something different when we reach a BREAK
# instruction
def newBreak(PC):

	while 1:
		decimalValue = readFile()	
		line = convert_to_binary(decimalValue) 
		a = line
		PC = PC +4
		count = 0;	
		bits = 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1
		i = 0
		address = 0
		if line[0] == '0':
		 while i < 11:
		  if line[i+21] == '1':	
		   address = address + bits[i]
		   data.append(address)
		  i = i + 1
		 #print i
		 print line,'     ',PC , address
		if line[0] == '1':
		 while i < 31:
		  i = i + 1
		  #if line[i] == '1':
		   #line[i] = 0
		  if line[i] == '0':
		   address = address + 2**(31-i)
		 address = address + 1
		 data.append(0 - address)
		 i = 0
		 print  line,'     ',PC , '-', address





# this defines the rest of the instructions
# notice it statements for LW and SW 
# i just wrote headers for an overloaded function
# to get the r values, but didn't complete it

def convert_to_instruction(line,PC):
	j, JR, BEQ, addi, bltz, sw, lw, mul,  = '00010', '01000', '00100', '01000', '00001', '01011', '00011', '11100'
	function = 'holder'
	if line[0] == '0':
	 function = 'invalid instruction'
#	 print line[0], line[1:6], line[6:11], line[11:16], line[16:21], line[21:26], line [26:32], PC, 'invalid instruction'
	if line[1:6] == '00000':
	 function = specOpCode(line[26:32])	
	if line[1:6] == j:
	 function = 'J'
	if line[1:6] == JR:		
	 function = 'JR'
	if line[1:6] == BEQ:
	 function = 'BEQ'
	if line[1:6] == addi:
	 function = 'ADDI'
	 immediate_addr = convert_imm_address(line[21:32])
	 rSW1 =  convert_r(line[11:16])
	 rSW2 =  convert_r(line[6:11])
	if line[1:6] == bltz:
	 function = 'BLTZ'
	if line[1:6] == sw:
	 function = 'SW'
	 immediate_addr = convert_imm_address(line[21:32])
	 rSW1 =  convert_r(line[11:16])
	 rSW2 =  convert_r(line[6:11])
	if line[1:6] == lw:
	 function = 'LW'
	 immediate_addr = convert_imm_address(line[21:32])
	 rLW1 =  convert_r(line[11:16])
	 rLW2 =  convert_r(line[6:11])
	if line[1:6] == mul:
	 function = 'MUL'
	

#	if  function  == 'J' or  function == 'JR' or  function == 'BEQ' or  function == 'ADDI' or  function == 'BLTZ' or function == 'MUL':
#	 	print line[0], line[1:6], line[6:11], line[11:16], line[16:21], line[21:26], line [26:32], PC, function, 'R','R','#' 
#	if function =='LW':
#	 	print line[0], line[1:6], line[6:11], line[11:16], line[16:21], line[21:26], line [26:32], PC, function,'R',rLW1, immediate_addr, '(R',rLW2,')'
#	if function =='SW':
#	 	print line[0], line[1:6], line[6:11], line[11:16], line[16:21], line[21:26], line [26:32], PC, function,'R',rSW1, immediate_addr, '(R',rSW2,')'
#	if function == 'BREAK':
#		newBreak(PC)
#	infile.close()
	
	return function

	 

# I guess this would be the 'MAIN'
#while 1:
#	decimalValue = readFile()		
#	line = convert_to_binary(decimalValue)	
#	function = convert_to_instruction(line,PC)
#	#output_cycle(registers, PC, function)
#	PC =PC +4


      


