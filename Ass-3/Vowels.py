# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 23:16:52 2020

@author: sumant
"""

inp=input("Enter a word: ").lower() # input taking from user

c = [",".join(i) for i in inp ] 

vowels=["a","e","i","o","u"]

for i in c:
    if i in vowels:
        print(i)

output=[ i for i in c if i in vowels]
print(output)
