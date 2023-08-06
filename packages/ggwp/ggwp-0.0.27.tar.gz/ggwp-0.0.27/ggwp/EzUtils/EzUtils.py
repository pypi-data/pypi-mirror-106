import pandas as pd
import numpy as np
# from resource.config import EzConfig
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

import os, sys
import json

python_path = os.path.realpath(__file__).split(os.sep)[:-3]
# print(python_path)
config_path = python_path + ['resource','config.json']
config_path = os.sep.join(config_path)

with open(config_path, 'r') as f:
    version = json.load(f)['version']

# version = "0.0.26"

class EzUtils:
    def __init__(self):
        self.__version__ = version
        pass
    
    def hello_world(self):
        print("hello world!!")

    def get_q1(self,x):
        return x.quantile(.25)

    def get_q3(self,x):
        return x.quantile(.75)