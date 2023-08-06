# import ggwp, os
# import configparser

# current = os.sep.join(ggwp.__file__.split(os.sep)[:-1])
# config_path  = '{0}/config/config.cfg'.format(current)
# parser = configparser.ConfigParser()
# parser.read(config_path)
# __version__ = parser['default']['version']


# class EzConfig:

#     def __init__(self):
#         self.__version__ = __version__

import ggwp
import os
import configparser

class EzConfig:
    def __init__(self):
        self.__path__ = ggwp.__file__

    def get_config(self, section, key):
        root = os.sep.join(self.__path__.split(os.sep)[:-1])
        config_path = f"{root}/config/config.cfg"
        parser = configparser.ConfigParser()
        parser.read(config_path)
        return parser[section][key]