postmem, postalu = '0', '0'
def write_back_unit(postmem, postalu, isempty ):
cyclenum = 0
#All of the register stuff.


#all of the out pust stuff is here I dont know why.
print '--------------------'
print 'Cycle:', cyclenum
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

cyclenum = cyclenum + 1
def instruction_fetch():



def issue():

def MEM():


def ALU():

