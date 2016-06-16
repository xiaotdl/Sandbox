# Ref:
# Python AES two-way encryption/decryption example
# https://gist.github.com/sekondus/4322469

from Crypto.Cipher import AES
import base64
import os

PASSWORD = 'let me in'

# the block size for the cipher object; must be 16, 24, or 32 for AES
BLOCK_SIZE = 32

# the character used for padding--with a block cipher such as AES, the value
# you encrypt must be a multiple of BLOCK_SIZE in length.  This character is
# used to ensure that your value is always a multiple of BLOCK_SIZE
PADDING = '{'

# one-liner to sufficiently pad the text to be encrypted
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

# one-liners to encrypt/encode and decrypt/decode a string
# encrypt with AES, encode with base64
encode_AES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
decode_AES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)

# generate a random secret key
secret = os.urandom(BLOCK_SIZE)

# create a cipher object using the random secret
cipher = AES.new(secret)

# encode a string
encoded = encode_AES(cipher, PASSWORD)
print 'Encrypted string:', encoded

# decode the encoded string
decoded = decode_AES(cipher, encoded)
print 'Decrypted string:', decoded


# >>>
# Encrypted string: QaG0D+wyFA0+Dvb/vXgD1bXDKoAbG5weyROvK2vs/Xw=
# Decrypted string: let me in
