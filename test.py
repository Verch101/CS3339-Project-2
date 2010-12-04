
from struct import *

f = open("test1.bin", "rb").read()
buf = f[3]
unpack('test1.bin', '\x00')


print buf
