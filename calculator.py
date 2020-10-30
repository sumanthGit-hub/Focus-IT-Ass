# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 22:33:32 2020

@author: sumant
"""

# Calculator

while True:
    print()
    print("Welcome To My Calculator")
    print("========================")
    print("1. ADD")
    print("2. SUB")
    print("3. MUL")
    print("4. DIV")
    print("0. Exit")
    option=int(input("Please Choose Operation: "))
    
    if option > 4:
        print("Invalid Key Operation.")
        break
    elif option == 0:
        print("Bye Welcome back..!")
        break
    
    num1=int(input("Enter number1: "))
    num2=int(input("Enter number2: "))
    if option == 1:
        print(num1+num2)
    elif option == 2:
        print(num1-num2)
    elif option == 3:
        print(num1*num2)
    elif option == 4:
        if num2 != 0:
            print(num1/num2)
        else:
            print("Can`t divided by zero")
    else:
        print("Invalid Key Operation.")
        
    choice = input("Do you want to perform more (yes or no)? ")
    if choice.lower() != 'yes':
        print("Bye Catch up later..!")
        break
    
