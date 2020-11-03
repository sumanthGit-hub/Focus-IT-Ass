# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 23:34:54 2020

@author: sumant
"""


# Student Progress Report

print("Welcome")
sub   = ["telugu","hindi","english","maths","science","social"]
marks=[]

for i in range(6):
    marks.append(int(input(f"Enter {sub[i]} marks: ")))

total = sum(marks)
avg = (total/600)*100
    
print("")
print("Details of Student Progress...!")
print("Student marks : ")
for i in range(6):
    print(f"{sub[i]} : {marks[i]}")
print("Student Total Marks: ",total)
print("Student Average: ",round(avg,2))