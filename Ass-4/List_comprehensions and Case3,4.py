# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 00:13:06 2020

@author: sumant
"""

# List Comprehensions

even=[x for x in range(1,21) if x%2==0]
print(even)

odd=[x for x in range(1,21) if x%2==1]
print(odd)

square=[x*x for x in range(1,21)]
print(square)

cubes=[x**3 for x in range(1,21)]
print(cubes)


user = input("Enter Word: ")
print(user.capitalize())
print(user.casefold())
print(user.upper())
print(user.title())


user1 = input("Enter Word: ")

for i in user1:
    if i.isupper() == True:
        print(i)
