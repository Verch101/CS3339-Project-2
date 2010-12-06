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

