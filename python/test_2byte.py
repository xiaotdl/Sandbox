def char2byte(c):
    return "{0:08b}".format(ord(c))

def str2byte(s):
    return " ".join(char2byte(c) for c in s)

s = 'hello world'
print ' '.join(c for c in s)
print ' '.join(str(ord(c)) for c in s)
print str2byte(s)

# >>>
# h e l l o   w o r l d
# 104 101 108 108 111 32 119 111 114 108 100
# 01101000 01100101 01101100 01101100 01101111 00100000 01110111 01101111 01110010 01101100 01100100

def int2byte(num):
    return "{0:08b}".format(num)
def byte2int(byte):
    return int(str(byte), 2)
print int2byte(5)
print int2byte(25)
print int2byte(28)
# >>>
# 00000101
# 00011001
# 00011100
print byte2int(int2byte(28))
# >>>
# 28
