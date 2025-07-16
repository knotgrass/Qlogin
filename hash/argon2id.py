import os
from argon2 import PasswordHasher
from argon2.profiles import RFC_9106_LOW_MEMORY, RFC_9106_HIGH_MEMORY, PRE_21_2, CHEAPEST


ph = PasswordHasher.from_parameters(RFC_9106_LOW_MEMORY)

password = "my_secure_password"
salt = os.urandom(16)
print(salt)
hash = ph.hash(password, salt=b"'\xd4\x00\xee\xb3g\x06\xefh\xb9\xfb\xf6\xe83$\x7f")
print(hash)
