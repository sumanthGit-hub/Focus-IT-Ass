# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 20:10:09 2020

@author: sumant
"""

list1=[1,2,3,4,"Sumanth","Mantu",1,2,3,2,3,4,2,3,4] # Dupicate values are available in this list
eliminate=set(list1)
print(eliminate) # we get output as set

# Another method
list3=[1,2,3,4,"Sumanth","Mantu",1,2,3,2,3,4,2,3,4] # Dupicate values are available in this list
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)   

# List Comprehension
list4=[1,2,3,4,"Sumanth","Mantu",1,2,3,2,3,4,2,3,4]
list5=[]
com=[ list5.append(i) for i in list4 if i not in list5]
print(list5)
