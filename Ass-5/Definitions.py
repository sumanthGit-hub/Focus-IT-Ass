# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 21:48:44 2020

@author: sumant
"""
num1=int(input("Enter number: "))
def even(num):
    """ function for printing even numbers """
    for i in range(1,num):
        if i%2==0:
            print("Even Number: ",i)
even(num1)

def odd(num):
    """ function for printing even numbers """
    for i in range(1,num):
        if i%2==1:
            print("Odd Number: ",i)
odd(num1)

###################################################################

num2 = int(input("Enter multiplication number: "))
def multi(num):
    """ function for multiplication table """
    for i in range(1,21):
        print(num,"*",i,"=",i*num)

multi(num2)

###################################################################

num3 = int(input("Enter number: "))
num4 = int(input("Enter number: "))
def maximum2(num1,num2):
    """ Finding max number """
    print("Max Number is ",max(num1,num2))

maximum2(num3,num4)

num5 = int(input("Enter number1: "))
num6 = int(input("Enter number2: "))
num7 = int(input("Enter number3: "))

def maximum3(num1,num2,num3):
    """ Finding max number """
    print("Max Number is ",max(num1,num2,num3))

maximum3(num5,num6,num7)

###################################################################

list1 = [1,2,3,12,34,45,67,78,90]
def max_element(l):
    """ Finding max number in list """
    print("Maximum element is ",max(list1))
    
max_element(list1)

list2 = (12,3,12,34,45,67,78,90)
def min_element(l):
    """ Finding max number in tuple """
    print("Minimun element is ",min(list1))
    
min_element(list2)

###################################################################

num7 = int(input("Enter number: "))
def factorial(num7):
    """ Calculating factorial of given number """
    fact = 1
    for i in range(1,num7+1): 
        fact = fact * i     
    print (f"The factorial of {num7} is : ",fact)

factorial(num7)

###################################################################

str1 = input("Enter string:")
def reverse_string(inp):
    """ Reversing the string """
    print(inp[::-1])
    
reverse_string(str1)

###################################################################

list2=[11,12,14,15,16,17,11,2,12,2,4,23,34,45,56,67,78,89]

def all(num):
    print("Sum of all numbers: ",sum(num))
    print("Reversed of list order: ",num[::-1])
    print("Length of List: ",len(list2))
    print("Count of number: ",num.count(2))
    
all(list2)













