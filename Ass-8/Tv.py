# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 09:37:03 2020

@author: sumanth
"""


class Tv:
    """ This is tv product data"""
    
    def __init__(self,model,brand):
        self.model = model
        self.brand = brand
        
    def features(self):
        print(f"{self.brand} Tv model {self.model}..!")
    

class SmartTv(Tv):
    """ This is smart features of tv """
    
    def __init__(self,model,brand,screenSize,resolution,price):
        super().__init__(model,brand)
        self.screenSize = screenSize
        self.price = price
        self.resolution = resolution


    def newFeatures(self):
        print("Smart Features of ",end="")
        super().features()
        print("Screensize: ",self.screenSize)
        print("Resolution: ",self.resolution)
        print("Price: ",self.price)
        
tv = SmartTv("A5","Samsung","50 inches","1920 × 1080",40000)
tv.newFeatures()
