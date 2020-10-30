# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 21:31:07 2020

@author: sumant
"""


# Student Progress Report

print("Welcome")
rollno= input("Enter RollNo: ")
name  = input("Enter Name: ")
sub   = ["telugu","hindi","english","maths","science","social"]
marks={}

for i in sub:
    marks[i]=int(input(f"Enter {i} marks: "))

total = sum(marks.values())

avg = (total/600)*100

grade = None
if avg >= 80 and avg <= 100:
    grade = "A"
elif avg >= 60 and avg <= 79:
    grade = 'B'
elif avg >= 50 and avg <= 59:
    grade = 'C'
elif avg >= 40 and avg <= 49:
    grade = 'D'
elif avg < 40:
    grade = 'Promoted'
    
print("")
print("Details of Student...!")
print("Student RollNo: ",rollno)
print("Student Name: ",name)
print("Student Total Marks: ",total)
print("Student Average: ",round(avg,2))
print("Student Grade",grade)

    
    












