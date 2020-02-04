import unittest
import tempfile
import string
import os
from random import choice, randint
from autoyaml import load_config, write_config
from autoyaml.encryptor import encrypt_file, decrypt_file

def random_string(stringLength=10, selection=string.ascii_lowercase):
    """Generate a random string of fixed length """
    return ''.join(choice(selection) for i in range(stringLength))



class TestAutoyamlMethods(unittest.TestCase):
    password = random_string()
    app      = random_string()
    config   = {"appname": app}
    enc_app      = random_string()
    enc_config   = {"appname": enc_app}
    
    def writer(self, name, encrypted=False):
        suffix = '' if not encrypted else '.enc'
        file_path = os.path.expanduser('~/.{}'.format(name)) + suffix
        if encrypted:
           return file_path
        with open(file_path,'w') as tmp:
           header = '---\n'
           file_contents = header + "{name}: {name}".format(name=name)
           tmp.write(file_contents)
        return file_path
        
    def password_function(self):
        return self.password

    def test_load_config(self):
        fname = self.writer(self.app)
        self.assertEqual(load_config(self.app),{self.app:self.app})
        os.remove(fname)
    
    def test_a_encrypt_config(self):
        write_config(self.enc_config, self.enc_app, encrypted=True, password_function=self.password_function)
        self.filename = self.writer(self.enc_app, encrypted=True)
        with open(self.filename) as filename:
           self.assertNotIn(self.enc_app, filename.read())

    def test_b_decrypt_config(self):
        loaded_config = load_config(self.enc_app, password_function=self.password_function) 
        self.assertEqual(loaded_config, self.enc_config)
        os.remove(self.writer(self.enc_app, encrypted=True))

    def test_write_config(self):
        write_config({self.app:self.app}, self.app) 
        write_config({self.app:'overwrite'}, self.app, overwrite=False)
        fname = os.path.expanduser('~/.{}'.format(self.app))
        with open(fname) as tmp:
           test_str = '---\n{app}: {app}\n'.format(app=self.app)
           read_str = tmp.read()
           self.assertEqual(test_str, read_str)
        os.remove(fname)

class TestEncryptorMethods(unittest.TestCase):
    file_name = '/tmp/test'
    contents  = random_string()
    password  = random_string()
    salt      = random_string(selection='0123456789')
    
    def test_a_encrypt(self):
       with open(self.file_name,'w') as test_file:
          test_file.write(self.contents)
       encrypt_file(self.file_name, self.password, self.salt)
       with open(self.file_name) as test_file:
          self.assertNotEqual(self.contents, test_file.read())

    def test_b_decrypt(self):
       decrypt_file(self.file_name, self.password, self.salt)
       with open(self.file_name) as test_file:
          self.assertEqual(self.contents, test_file.read())

if __name__ == '__main__':
    unittest.main()
