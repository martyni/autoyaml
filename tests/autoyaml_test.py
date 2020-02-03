import unittest
import tempfile
import string
import os
from random import choice, randint
from autoyaml import load_config, write_config
from autoyaml.encryptor import encrypt, decrypt

def random_string(stringLength=10, selection=string.ascii_lowercase):
    """Generate a random string of fixed length """
    return ''.join(choice(selection) for i in range(stringLength))



class TestAutoyamlMethods(unittest.TestCase):
    
    def writer(self, name):
        file_path = os.path.expanduser('~/.{}'.format(name))
        with open(file_path,'w') as tmp:
           header = '---\n'
           file_contents = header + "{name}: {name}".format(name=name)
           tmp.write(file_contents)
        return file_path
        

    def test_load_config(self):
        app = random_string()
        fname = self.writer(app)
        self.assertEqual(load_config(app),{app:app})
        os.remove(fname)

    def test_write_config(self):
        app = random_string()
        write_config({app:app}, app) 
        write_config({app:'overwrite'}, app, overwrite=False)
        fname = os.path.expanduser('~/.{}'.format(app))
        with open(fname) as tmp:
           test_str = '---\n{app}: {app}\n'.format(app=app)
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
       encrypt(self.file_name, self.password, self.salt)
       with open(self.file_name) as test_file:
          self.assertNotEqual(self.contents, test_file.read())

    def test_b_decrypt(self):
       decrypt(self.file_name, self.password, self.salt)
       with open(self.file_name) as test_file:
          self.assertEqual(self.contents, test_file.read())

if __name__ == '__main__':
    unittest.main()
