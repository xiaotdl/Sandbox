import string

table = string.maketrans(
    string.ascii_lowercase,
    string.ascii_lowercase[2:]+string.ascii_lowercase[:2]
)

def decipher(s):
    deciphered_s = ""
    for char in s:
        if char.isalpha():
            deciphered_s += chr((ord(char)-ord('a') + 2) % 26 + ord('a'))
        else:
            deciphered_s += char
    return deciphered_s


s = "http://www.pythonchallenge.com/pc/def/map.html"
print '== original string =='
print s
print '== deciphered string == string.translate(s, table)'
print string.translate(s, table)
print '== deciphered string == decipher(s)'
print decipher(s)

# >>>
# == original string ==
# http://www.pythonchallenge.com/pc/def/map.html
# == deciphered string == string.translate(s, table)
# jvvr://yyy.ravjqpejcnngpig.eqo/re/fgh/ocr.jvon
# == deciphered string == decipher(s)
# jvvr://yyy.ravjqpejcnngpig.eqo/re/fgh/ocr.jvon
