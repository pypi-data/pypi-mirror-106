import pandas as pd
import numpy as np

from ggwp.config.config import EzConfig

version = EzConfig().__version__

class EzUtils:
    def __init__(self):
        self.__version__ = version
    
    def hello_world(self):
        print("hello world!!")

    def get_q1(self,x):
        return x.quantile(.25)

    def get_q3(self,x):
        return x.quantile(.75)