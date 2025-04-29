from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

simple_key = get_random_bytes(32)
print(simple_key)

salt = b'\x18&+ \x135\x9fE\xc0\x81\xaa\xc2?\x03\x9dK\x9ftgg\xfa\x88<\xaf\x12z\xee\x80\xdc\xf8\x9e8'
password = "titanic"

key = PBKDF2(password, salt, dkLen=32)
message = b"Hello secret world"

cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(message, AES.block_size))

with open('encrypted.bin', 'wb') as f:
    f.write(cipher.iv)
    f.write(ciphered_data)


with open('encrypted.bin', 'rb') as f:
    iv = f.read(16)
    decrypt_data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)
print(original)

with open('key.bin', 'wb') as f:
    f.write(key)



