# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 00:02:28 2020

@author: sumant
"""


print("My To Do App")
print("============")
print("1. Add Task")
print("2. View All Tasks")
print("0. Exit")


task_list={}
while True:
    opt = int(input("Please Choose option: "))

    if opt == 1:
        task = input("Enter task name: ")
        task_list[task] = input("Enter Date(DD/MM/YYYY): ")
        print("Task added")
    
    elif opt == 2:
        print("Task Name   Task Date")
        print("---------   ---------")
        for i,j in task_list.items():
            print(f"{i}     {j}")
            
    elif opt == 0:
        print("Bye")
        break
    else:
        print("Invalid Choice Bye..!")
        break