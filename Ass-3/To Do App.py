# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 23:44:41 2020

@author: sumant
"""

print("My To Do App")
print("============")
print("1. Add Task")
print("2. View All Tasks")
print("0. Exit")


task_list=[]
while True:
    opt = int(input("Please Choose option: "))

    if opt == 1:
        task = input("Enter task name: ")
        task_list.append(task)
        print("Task added")
    
    elif opt == 2:
        print("Task Name : ")
        print("-------------")
        for i in range(len(task_list)):
            print(f"{i+1}. {task_list[i]}")
            
    elif opt == 0:
        print("Bye")
        break
    else:
        print("Invalid Choice Bye..!")
        break