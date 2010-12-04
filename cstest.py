from struct import *
import os, os.path, stat


# Trying to read the first bit of each line to see what to excitute
add, j, JR, BEQ, addi  ='00000', '00010', '01000', '00100', '01000'
PC = 96
registers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
a = -1
infile = open("test1.bin",'rb')
dis = open("DIS.txt", 'w')

#returns the total number of lines in the file
def readLength():
	fileLength = os.stat('test1.bin')[6]
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

def convert_ADDI(line):
	bits = 32, 16, 8, 4, 2, 1
	# 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024
	#1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1
	i = 0
	r = 0
	while i < 6:
		if line[i] == '1':	
			r = r + bits[i]
		i = i + 1
		#print i
		if r == 63:
			r = (-1)
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
		 print>>dis, line,'     ',PC , address
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
		 print>>dis,  line,'     ',PC , '-', address





# this defines the rest of the instructions
# notice it statements for LW and SW 
# i just wrote headers for an overloaded function
# to get the r values, but didn't complete it 

def convert_to_instruction(line,PC):
	#dis = open("DIS.txt", 'w')
	j, JR, BEQ, addi, bltz, sw, lw, mul,  = '00010', '01000', '00100', '01000', '00001', '01011', '00011', '11100'
	function = 'holder'
	
	if line[1:6] == j:
	 	function = 'J'
		immediate_addr = convert_ADDI(line[26:32]) * 4
	
	if line[1:6] == JR:		
	 	function = 'JR'
		immediate_addr = convert_ADDI(line[26:32]) * 4
	
	if line[1:6] == BEQ:
	 	function = 'BEQ'
	 	immediate_addr = convert_ADDI(line[26:32]) * 4
	 	rBRANCH =  convert_r(line[6:11])
	
	if line[1:6] == addi:
	 	function = 'ADDI'
	 	immediate_addr = convert_ADDI(line[26:32])
	 	rADDSL1 =  convert_r(line[11:16])
	 	rADDSL2 =  convert_r(line[6:11])
	
	if line[1:6] == bltz:
	 	function = 'BLTZ'
	 	immediate_addr = convert_ADDI(line[26:32]) * 4
	 	rBRANCH =  convert_r(line[6:11])
	
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

###############################################################################
###############################################################################
	if line[0] == '0':
	 	print>>dis, line[0], line[1:6], line[6:11], line[11:16], line[16:21], line[21:26], line [26:32], PC, 'invalid instruction'
		function = 'holder'
	
	if line[1:6] == '00000':
	 	function = specOpCode(line[26:32])
	
	if  function  == 'J' or function == 'JR':
	 	print>>dis, line[0], line[1:6], line[6:11], line[11:16], line[16:21], line[21:26], line [26:32], PC, function, '#',immediate_addr  	
	
	if  function == 'ADDI':
		#immediate_addr = convert_r(line[26:31])
	 	#rADDSL1 =  convert_r(line[11:16])
	 	#rADDSL2 =  convert_r(line[6:11])
	 	print>>dis, line[0], line[1:6], line[6:11], line[11:16], line[16:21], line[21:26], line [26:32], PC, function, 'R',rADDSL1, 'R', rADDSL2, '#',immediate_addr  
	
	if  function == 'BLTZ' or  function == 'BEQ':
		print>>dis, line[0], line[1:6], line[6:11], line[11:16], line[16:21], line[21:26], line [26:32], PC, function, 'R',rBRANCH,'#', immediate_addr 
	
	if  function == 'ADD' or function == 'SUB':
		rADDSUB1 =  convert_r(line[11:16])
	 	rADDSUB2 =  convert_r(line[6:11])
		rADDSUB3 =  convert_r(line[11:16])
		print>>dis, line[0], line[1:6], line[6:11], line[11:16], line[16:21], line[21:26], line[26:32], PC, function ,'R',rADDSUB1,'R',rADDSUB2,'R',rADDSUB3
	
	if function == 'SLL' or function == 'SRL':
		immediate_addr = convert_r(line[21:26])
	 	rADDSL1 =  convert_r(line[11:16])
	 	rADDSL2 =  convert_r(line[6:11])
		print>>dis, line[0], line[1:6], line[6:11], line[11:16], line[16:21], line[21:26], line [26:32], PC, function, 'R',rADDSL1, 'R', rADDSL2, '#',immediate_addr   
	
	if function == 'MUL':
	 	print>>dis, line[0], line[1:6], line[6:11], line[11:16], line[16:21], line[21:26], line [26:32], PC, function 
	
	if function =='LW':
	 	print>>dis, line[0], line[1:6], line[6:11], line[11:16], line[16:21], line[21:26], line [26:32], PC, function,'R',rLW1, immediate_addr, '(R',rLW2,')'
	
	if function =='SW':
	 	print>>dis, line[0], line[1:6], line[6:11], line[11:16], line[16:21], line[21:26], line [26:32], PC, function,'R',rSW1, immediate_addr, '(R',rSW2,')'
	
	if function == 'BREAK':
		newBreak(PC)
		infile.close()
		
	PC = PC + 4
	#return function

	 

######################################################################
####################################################################
#####################################################################
# Arguements to pass that may be helpful are the current cycle count, the PC, the function (ie addi)
# Also will want to call a function that looks at the function(addi) and based on what function it is, will output the correct rs, rt, rd, and immediate?


def output_cycle(registers, PC, function):

# Creates and opens file "cycle" in the /tmp/output directory with the write capability
	cycle = open("output.txt", 'w')
	print>>cycle, 'ttr'
	count =1

# While loop: Needs to exit the loop after the break cycle

# Prints the header of the cycle file
	cycle.write("====================")
	header = "cycle: ", count, PC, "	", function, "R1, R0, #10 \n"

# Prints the registers and their contents, must access the previously created array registers[] size = 32 elements
	cycle.write("registers: \n")

	r00 = "r00:", registers[0], "	", registers[1], "   ",registers[2], "   ",registers[3], "   ",registers[4], "   ",registers[5], "   ",registers[6], "   ",registers[7], "      \n"
	r08 = "r08:", registers[8], "   ", registers[9], "   ",registers[10], "   ",registers[11], "   ",registers[12], "   ",registers[13], "   ",registers[14], "   ",registers[15], "      \n"
	r16 = "r16", registers[16], "	", registers[17], "	",registers[18], "   ",registers[19], "   ",registers[20], "   ",registers[21], "   ",registers[22], "   ",registers[23], "      \n"
	r24 = "r24:", registers[24], "   ", registers[25], "   ",registers[26], "   ",registers[27], "   ",registers[28], "   ",registers[29], "   ",registers[30], "   ",registers[31], "	\n"

	print>>cycle, (r00[1])
	print>>cycle, (r08)
	print>>cycle, (r16)
	print>>cycle, (r24)

# Prints the data and its contents, must access the previously created array data[] size = 24 elements 
	data172 = '172:', data[0],"    ", data[1],"    ", data[2],"    ", data[3],"    ", data[4],"    ", data[5],"    ", data[6],"    ", data[7],"    \n"
	data204 = "204:", data[8],"    ", data[9],"    ", data[10],"    ", data[11],"    ", data[12],"    ", data[13],"    ", data[14],"    ", data[15],"    \n"
	data205 = "236:", data[16],"    ", data[17],"    ", data[18],"    ", data[19],"    ", data[20],"    ", data[21],"    ", data[22],"    ", data[23],"    \n"

	print>>cycle, (data172)
	print>>cycle, (data204)
	print>>cycle, (data205)
	count = count +1
	
# Must close the file to free up memory
	cycle.close()


####################################################################3
#################################################################
####################################################################




# I guess this would be the 'MAIN'
while 1:
	
	decimalValue = readFile()	
	line = convert_to_binary(decimalValue)
	#function = convert_to_instruction(line,PC)
	convert_to_binary(decimalValue)
	convert_to_instruction(line,PC)
	PC = PC + 4
	#dis.close()
	
	#output_cycle(registers, PC, function)



      


