# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 22:55:57 2020

@author: sumant
"""

import csv

#### Creating CSV file with some data ###########

with open("emp.csv","w",newline='') as f:
    w=csv.writer(f)
    w.writerow(["ID","NAME","SAL"])
    num=int(input("Enter Number of Details: "))
    for i in range(num):
        id=input("Enter ID No:")
        name=input("Enter Name:")
        sal=input("Enter Salary:")
        w.writerow([id,name,sal])
    print("Total Details written to csv file successfully")


######## Finding whose salary is empty ###############

with open("emp.csv","r",newline='') as f:
    w = csv.reader(f)
    data = list(w)
    print(data[0][0:])
    for line in data:
        if line[2] == '':
            print(line)

######## Finding whose salary is greater than 3500 ###############

with open("emp.csv","r",newline='') as f:
    w = csv.reader(f)
    data = list(w)
    data1 = data[1:]
    print(data[0][0:])
    for line in data1[0:]:
        if line[2] != "":
            if int(line[2]) > 3500:
                print(line)

######## Finding whose name starts with ‘A’ ###############

with open("emp.csv","r",newline='') as f:
    w = csv.reader(f)
    data = list(w)
    print(data[0][0:])
    for line in data:
        if line[1].startswith("A"):
            print(line)

######## Finding whose id or name or sal is empty ###############

with open("emp.csv","r",newline='') as f:
    w = csv.reader(f)
    data = list(w)
    print(data[0][0:])
    for line in data:
        if line[0]  == '' or line[1]  == '' or line[2] == '':
            print(line)

######## Finding whose id or name or sal is not empty ###############

with open("emp.csv","r",newline='') as f:
    w = csv.reader(f)
    data = list(w)
    for line in data:
        if line[0]  != '' and line[1]  != '' and line[2] != '':
            print(line)
            
            
