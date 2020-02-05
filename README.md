# autoyaml because config should be easy
Autoconfig is a config generator that takes
a dictionary, writes it to a file and loads it
back as a dictionary. 

The aim of this project is to standardise the
way python projects create and feed parameters into 
python applications without having to 
rewrite the same IO functions every time. 


## Installation
```
pip install autoyaml
```

## Usage
Write your config either from an interactive terminal
or from a script
```
from autoyaml import write_config

conf = {
   'parameter1': 1,
   'parameter2': 'something'
}

application_name = 'app_name'

write_config(conf,application_name)
```
Load your config from another python application
```
from autoyaml import load_config

class My_Class(object):
   def __init__(self, **kwargs):
      self.parameter1 = kwargs['parameter1']
      self.parameter2 = kwargs['parameter2']
      self.show_parameters()

   def show_parameters(self):
      print('parameter1 : {}'.format(self.parameter1))
      print('parameter2 : {}'.format(self.parameter2))


if __name__ == "__main__":
   my_class = My_Class(**load_config('app_name'))
```
## Password Protected Encryption
```
from autoyaml import write_config
from getpass import getpass

conf = {
   'secret_key': getpass('Secret Key? ')
}

application_name = 'app_name1'

write_config(conf, application_name, encrypted=True)

```
## Loads the same but requires password input by default
```
from autoyaml import load_config

class My_Class(object):
   def __init__(self, **kwargs):
      self.secret_key = kwargs['secret_key']
      self.show_parameters()

   def show_parameters(self):
      print('the last character of your secret it {}'.format(self.secret_key[-1]))


if __name__ == "__main__":
   my_class = My_Class(**load_config('app_name1'))
```
## Create a custom password function 
```
from autoyaml import load_config, write_config
def BAD_PASSWORD_FUNCTION():
   return 'password123'

write_config({'foo':'bar'},'app_name2', encrypted=True, password_function=BAD_PASSWORD_FUNCTION)

print(load_config('app_name3', password_function=BAD_PASSWORD_FUNCTION)
```
