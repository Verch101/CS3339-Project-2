<<<<<<< HEAD
postmem, postalu = '0', '0'
def write_back_unit(postmem, postalu, isempty ):
cyclenum = 0
#All of the register stuff.


#all of the out pust stuff is here I dont know why.
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
print '        Entry 1:', postALUbuffer1
print 'Pre_MEM Queue:'
print '        Entry 0:', preMEMbuffer0
print '        Entry 1:', preMEMbuffer1
print 'Post_MEM Queue:'
print '        Entry 0:', postMEMbuffer0
print '        Entry 1:', postMEMbuffer1
print ' '
print 'Registers'
print 'R00:', '        ', registers[0],'        ', registers[1],'        ', registers[2],'        ', registers[3],'        ', registers[4],'        ', registers[5],'        ', registers[6],'        ', registers[7]
print 'R08:', '        ', registers[8],'        ', registers[9],'        ', registers[10],'        ', registers[11],'        ', registers[12],'        ', registers[13],'        ', registers[14],'        ', registers[15]
print 'R16:', '        ', registers[16],'        ', registers[17],'        ', registers[18],'        ', registers[19],'        ', registers[20],'        ', registers[21],'        ', registers[22],'        ', registers[23]
print 'R24:', '        ', registers[24],'        ', registers[25],'        ', registers[26],'        ', registers[27],'        ', registers[28],'        ', registers[29],'        ', registers[30],'        ', registers[31]

#Cash stuff goes here But I dont understand that stuff yet, so this is just a black hole for right now. We can just put something in here later to make the diff closer.

print 'Data'
print '128:	4	16
print '--------------------'

cyclenum = cyclenum + 1
def instruction_fetch():



def issue():

def MEM():


def ALU():

=======
from cstest.py import *
PC = 96

if (len(sys.argv) > 1):
	bin_file, dis_file = sys.argv[1], sys.argv[2]
else:
 	print "Please enter valid input/output files"


def instruction_fetch():

	x = 0	
	while x<2:
		decimalValue = readFile()	
		line = convert_to_binary(decimalValue)
		#convert_to_binary(decimalValue)
		#convert_to_instruction(line,PC)
		PC = PC + 4
		function = convert_to_instruction(line,PC)
		if (x == 0):
			IF_BIN_ONE = line
			IF_INST_ONE = function
		if (x == 1):
			IF_BIN_TWO = line
			IF_INST_TWO = function
		output_cycle(registers, PC, function)
		x = x + 1
	print "two instructions were just loaded into the IF"
	print "they are", IF_INST_ONE, "and", IF_INST_TWO



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
