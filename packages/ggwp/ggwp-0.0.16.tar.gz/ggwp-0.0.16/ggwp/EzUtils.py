class EzUtils:
    def __init__(self):
        self.__version__ = "0.0.15"
    
    def hello_world(self):
        print("hello world!!")

    def get_q1(self,x):
        return x.quantile(.25)

    def get_q3(self,x):
        return x.quantile(.75)