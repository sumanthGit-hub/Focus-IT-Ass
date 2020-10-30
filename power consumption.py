# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 00:09:05 2020

@author: sumant
"""

# Power consumption calc app

units=int(input("Enter number of units consumed: "))
amount=[]

if units >= 1 and units <=50:
    amount.append(3*units)
elif units >= 51 and units <= 100:
    amount.append(3*50)
    c1 = units-50
    amount.append(c1*6)
elif units >= 101 and units <= 150:
    amount.append(3*50)
    amount.append(6*50)
    c1 = units-100
    amount.append(9*c1)
elif units >= 151 and units <= 200:
    amount.append(3*50)
    amount.append(6*50)
    amount.append(9*50)
    c1 = units-150
    amount.append(12*c1)
elif units > 200:
    amount.append(3*50)
    amount.append(6*50)
    amount.append(9*50)
    amount.append(12*50)
    c1 = units-200
    amount.append(12*c1)

print()
print("Bill Details -->")
print("Total units consumed: ",units)
print("Bill Amount: ",sum(amount))