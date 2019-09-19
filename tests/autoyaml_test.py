import unittest
import tempfile
import string
import os
from random import choice, randint
from autoyaml import load_config, write_config


def random_string(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(choice(letters) for i in range(stringLength))



class TestStringMethods(unittest.TestCase):
    
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

if __name__ == '__main__':
    unittest.main()
