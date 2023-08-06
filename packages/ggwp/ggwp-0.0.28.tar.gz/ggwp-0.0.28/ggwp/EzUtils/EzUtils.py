import pandas as pd
import numpy as np

version = "0.0.28"

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