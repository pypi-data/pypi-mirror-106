import pandas as pd
import numpy as np

# import configparser

# config_path = '../resource/config.properties'
# # read config
# parser = configparser.ConfigParser()
# parser.read(config_path)
# config = parser['default']
# version = config['version']

class EzUtils:
    def __init__(self):
        self.__version__ = "0.0.24"
    
    def hello_world(self):
        print("hello world!!")

    def get_q1(self,x):
        return x.quantile(.25)

    def get_q3(self,x):
        return x.quantile(.75)