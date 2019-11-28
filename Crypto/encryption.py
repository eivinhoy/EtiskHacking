from Crypto.Cipher import DES
from Crypto import Random
import binascii

# block cipher

def des_ecb_encrypt(key, plaintext):
    # key must be 8 bytes
    # plaintext must be a multiple of 8 in length 
    des = DES.new(key, DES.MODE_ECB)
    ciphertext = des.encrypt(plaintext)
    return binascii.hexlify(ciphertext)


print(des_ecb_encrypt("01234567", "abcdefghijklmnop"))



def des_cfb_encrypt(key, plaintext):
    iv = Random.get_random_bytes(8)
    des = DES.new(key, DES.MODE_CFB, iv)
    ciphertext = des.encrypt(plaintext)
    return binascii.hexlify(ciphertext)


print(des_cfb_encrypt("01234567", "abcdefghijklmnop"))
