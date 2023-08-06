from resource.config import EzConfig
import pandas as pd
import numpy as np
from resource.config import EzConfig
# import json

# import configparser

# config_path = '../resource/config.properties'
# # read config
# parser = configparser.ConfigParser()
# parser.read(config_path)
# config = parser['default']
# version = config['version']

# with open("./resource/config.json") as configfile:
#     version = json.load(configfile)["version"]

class EzUtils:
    def __init__(self):
        self.__version__ = EzConfig().__version__
        pass
    
    def hello_world(self):
        print("hello world!!")

    def get_q1(self,x):
        return x.quantile(.25)

    def get_q3(self,x):
        return x.quantile(.75)