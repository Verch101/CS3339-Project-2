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
