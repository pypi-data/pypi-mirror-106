import pandas as pd
import numpy as np

import configparser

config_path  = './resource/config.cfg'
parser = configparser.ConfigParser()
parser.read(config_path)
version = parser['default']['version']

# from ggwp.config.config import EzConfig

# version = EzConfig().__version__

class EzUtils:
    def __init__(self):
        self.__version__ = version
    
    def hello_world(self):
        print("hello world!!")

    def get_q1(self,x):
        return x.quantile(.25)

    def get_q3(self,x):
        return x.quantile(.75)