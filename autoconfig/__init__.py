import os
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def __return_file_path(file_path, app):
    """
    Expands the ~/ into current users home directory
    """
    return os.path.expanduser(file_path.format(app))


def load_config(app, config_file='~/.{}'):
    """load yaml formatted config from a file

    arguments:
    appname -- name of the app being loaded
    
    keyword arguments:
    config_file -- path to the actual config file. Default "~/.{}"

    This function by defualt will look for a hidden
    file in the users home directory with that appname
    e.g
    load_config("app")
    will look in ~/.app and return a dictionary if the contents are 
    yaml formatted
    """
    config_filename = __return_file_path(config_file, app)
    try:
        with open(config_filename) as config:
            return load(config.read(), Loader=Loader)
    except FileNotFoundError:
        return {}


def write_config(config, app, config_file='~/.{}', overwrite=True):
    """write yaml formatted config to a file

    arguments:
    config  -- dictionary of config parameters
    appname -- name of the app the config is written for
    
    keyword arguments:
    config_file -- path to the actual config file. Default "~/.{}"
    overwrite   -- whether the config in the file should be 
                   overwritten or if only new parameters should 
                   be added. Default True 

    This function by defualt will write to a hidden
    file in the users home directory with that appname
    e.g
    write_config({"config": True}, "app")
    will write in ~/.app the dictionary in yaml format
    --- 
    config: true
    """
    config_filename = __return_file_path(config_file, app)
    current_config = load_config(app, config_file)
    if overwrite:
        current_config.update(config)
    else:
        config.update(current_config)
        current_config = config
    with open(config_filename, 'w+') as config_file:
        dump(
            current_config,
            config_file,
            default_flow_style=False,
            explicit_start=True
        )
    return current_config
