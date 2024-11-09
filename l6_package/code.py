import numpy as np

class calculator:
    """A class representing a calculator"""

    def __init__(self,initial_value=0):
        self.value=initial_value 
    
    def add(self,add):
        self.value += add
        return self.value

    def subtract(self,subtract):
        self.value -= subtract
        return self.value
    
    def divide(self,divide):
        self.value /= divide
        return self.value
    
    def multiply(self,multiply):
        self.value *= multiply
        return self.value
    
