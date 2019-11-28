from Crypto.Hash import SHA256
import hashlib
import binascii
import time


# hashing with SHA256
def hash(plaintext):
    origin_time = time.time()
    sha = SHA256.new(plaintext.encode()).hexdigest()
    time_interval = time.time() - origin_time
    print("mode - {0}".format(time_interval))
    return sha


print(hash("abc"))

# checking if hashes are identical
def check_password(plain, hashed):
    return SHA256.new(plain.encode()).hexdigest() == hashed


print(check_password("abc", hash("abc")))

# key derivation with salt 
def derived_key_hash(plaintext, salt, iterations):
    origin_time = time.time()
    derived_key = hashlib.pbkdf2_hmac('sha256', plaintext.encode(), salt.encode(), iterations)
    time_interval = time.time() - origin_time
    print("time - {0}".format(time_interval))
    return binascii.hexlify(derived_key)

print(derived_key_hash("abc", "salt", 1000000))