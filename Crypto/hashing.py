from Crypto.Hash import SHA256
import hashlib
import binascii


# hashing with SHA256
def hash(plaintext):
    return SHA256.new(plaintext.encode()).hexdigest()


print(hash("abc"))

# checking if hashes are identical
def check_password(plain, hashed):
    return SHA256.new(plain.encode()).hexdigest() == hashed


print(check_password("abc", hash("abc")))

# key derivation with salt 
def derived_key_hash(plaintext, salt, iterations):
    derived_key = hashlib.pbkdf2_hmac('sha256', plaintext.encode(), salt.encode(), iterations)
    return binascii.hexlify(derived_key)

print(derived_key_hash("abc", "salt", 100000))