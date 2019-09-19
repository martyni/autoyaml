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
git clone git@github.com:martyni/autoyaml.git
cd autoyaml
pip install .
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
