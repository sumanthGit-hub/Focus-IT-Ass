# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 08:30:36 2020

@author: sumant
"""


class Car:
    """ This is details of car data"""
    
    def __init__(self,model,brand,color):
        self.model = model
        self.brand = brand
        self.color = color
        
    def start(self):
        print(f"{self.color} color {self.brand} {self.model} model has starting..!")
    
    def move(self):
        print(f"{self.color} color {self.brand} {self.model} model has moving..!")
    
    def stop(self):
        print(f"{self.color} color {self.brand} {self.model} model has stoped..!")


class BMW(Car):
    """ This is Controls of car data"""
    
    def __init__(self,model,brand,color):
        super().__init__(model,brand,color)


    def autoPilot(self):
        print("Auto Pilot Started")
        print(f"{self.color} color {self.brand} {self.model} model has started and moving.")
    
    def autoGear(self):
        print("AutoGear has started")
        super().move()

            
b = BMW("B9","Audii","yellow")
b.autoPilot()
b.autoGear()



