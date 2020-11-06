# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 21:45:02 2020

@author: sumant
"""
########## Creating & Multiplying 2D matrix ########################### 

import numpy as np

row = int(input("Enter Number of Rows: ")) # Rows
col = int(input("Enter Number of columns: ")) # Columns

list1=[]
for i in range(row*col):
    num = int(input("Enter Nnumber: "))
    list1.append(num)
    
Array = np.array(list1) # Converting into array
A = Array.reshape(row,col) # Reshaping
print(A)

mul = int(input("Enter Multiply Number: "))

print("Multiply Matrix: \n",A*mul) # Multiplying


################### Pie Graph Covid Cases #############################

import matplotlib.pyplot as plt

colors = ["red","blue","purple","yellow","brown","pink","orange","green"] 

countries = ["United States","India","Brazil","Russia",
             "France","France","Argentina","United Kingdom"]

cases = [9937294,8439389,5617844,1733440,
         1601367,1365895,1217028,1146484]

plt.pie(cases,labels=countries,colors=colors,autopct="%1.2f%%")
plt.show()

# plt.bar(countries,height=cases,width=0.7)
# plt.show()

