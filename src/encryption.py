import base64
from Crypto.Cipher import AES
from Crypto import Random
import os

key = os.urandom(AES.block_size*2)
BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[:-ord(s[len(s)-1:])]
def encrypt(raw):
    raw = pad(raw)
    iv = Random.new().read( AES.block_size )
    cipher = AES.new(key, AES.MODE_CBC, iv )
    return base64.b64encode( iv + cipher.encrypt( raw ) ) 

def decrypt(enc):
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv )
    return unpad(cipher.decrypt( enc[16:] ))

f= open('1.jpg')
plain = f.read()
cipher = encrypt(plain)

fOut = open('encrypted','w')
fOut.write(cipher)
fOut.close()

f= open('encrypted')
cipher = f.read()
decrypted = open('decrypted', 'w')
decrypted.write(decrypt(cipher))
decrypted.close()

