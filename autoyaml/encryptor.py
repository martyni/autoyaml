import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from getpass import getpass

def __read_file(filename):
   with open(filename) as a_file:
      return a_file.read()

def __write_file(filename, contents):
   with open(filename, 'wb') as a_file:
      a_file.write(contents)

def setup(password, salt):
   password = password.encode()
   salt = salt.encode()
   kdf = PBKDF2HMAC(
     algorithm=hashes.SHA256(),
     length=32,
     salt=salt,
     iterations=100000,
     backend=default_backend()
   )
   key = base64.urlsafe_b64encode(kdf.derive(password))
   return salt, key

def encrypt(filename, password, salt):
   salt, key = setup(password, salt)
   contents = bytes(__read_file(filename),'utf-8')
   fernet = Fernet(key)
   __write_file(filename, fernet.encrypt(contents))
   
def decrypt(filename, password, salt):
   salt, key = setup(password, salt)
   contents = bytes(__read_file(filename),'utf-8')
   fernet = Fernet(key)
   __write_file(filename, fernet.decrypt(contents))
    
if __name__ == "__main__":
   with open('test', 'w') as test:
      test.write('1234')
   encrypt('test', getpass('password? '), '1234567890')
   with open('test') as test:
      print(test.read())
   decrypt('test', getpass('password? '), '1234567890')
   with open('test') as test:
      print(test.read())
