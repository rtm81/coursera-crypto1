import sys


CBC_key = "140b41b22a29beb4061bda66b6747e14"
CBC_Ciphertext_1 = "4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81"


from Crypto.Cipher import AES
from Crypto import Random

IV = Random.new().read(16)

obj2 = AES.new(CBC_key, AES.MODE_CBC, IV)
deciphered = obj2.decrypt(CBC_Ciphertext_1)
print(deciphered)
