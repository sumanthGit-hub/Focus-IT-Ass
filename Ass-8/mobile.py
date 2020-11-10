# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 09:57:08 2020

@author: sumant
"""

class Memory:
    """ This is Memory data """
    
    def __init__(self,internal,secondary,ram):
        self.internal = internal
        self.secondary = secondary
        self.ram = ram
        
    def details(self):
        print(f"Internal Memory: {self.internal}")
        print(f"Secondary Memory: {self.secondary}")
        print(f"Ram: {self.ram}")
    

class Mobile:
    """ This is details of mobile data"""
    
    def __init__(self,model,brand,price,memory):
        self.model = model
        self.brand = brand
        self.price = price
        self.memory = memory


    def newFeatures(self):
        print(f"Features of {self.brand} Model {self.model}")
        self.memory.details()
        print("Price: ",self.price)

m = Memory('128gb','256gb','6gb')
tv = Mobile("G5s","Moto",40000,m)
tv.newFeatures()




