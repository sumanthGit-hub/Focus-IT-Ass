# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 22:35:01 2020

@author: sumant
"""


with open("mytask.txt",'w') as f:
    f.write("Task Name : \n")
    f.write("------------\n")



while True:
    print("My To Do App")
    print("============")
    print("1. Add Task")
    print("2. View All Tasks")
    print("0. Exit")
    opt = int(input("Please Choose option: "))

    if opt == 1:
        task = input("Enter task name: ")
        with open("mytask.txt",'a') as f:
            f.write(f"{task}\n")
        print("Task added")
    
    elif opt == 2:
        with open("mytask.txt",'r') as f:
            task_list=f.read()
            print(task_list)
            
    elif opt == 0:
        print("Bye")
        break
    else:
        print("Invalid Choice Bye..!")
        break


