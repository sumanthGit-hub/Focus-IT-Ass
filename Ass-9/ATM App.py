# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 11:55:03 2020

@author: sumant
"""

class LimitExceedException(Exception):
    def __init__(self,arg):
        self.arg = arg
        
class InvalidMinimumException(Exception):
    def __init__(self,arg):
        self.arg = arg
        
class InsufficientFundException(Exception):
    def __init__(self,arg,bal):
        self.arg = arg
        self.bal = bal



print("ATM App")
print("1. To Deposit")
print("2. To Withdraw")
print("3. To Balance")
print("0. To Exit")

 
def ATM():
    bal = 100000
    option = int(input("Enter your option: "))
    if option == 1:
        amount = int(input("Enter Amount to deposit: "))
        print("Deposited Amount is ",amount)
        bal = bal+amount
        print("Total Amount is ",bal)
            
    elif option == 2:
        amt = int(input("Enter Amount: "))
        if amt > bal:
            raise InsufficientFundException("Insufficient Funds: Your balance is ",bal)
        elif amt < 100:
            raise InvalidMinimumException("Invalid Minimum Amount")
        elif amt > 10000:
            raise LimitExceedException("Limit Exceed: Enter less amount")
            
        else:
            bal = bal - amt
            print("Amount withdraw is Sucess")
            print("Remaining balance is ",bal)
    elif option == 3: 
        print("Account balance is :",bal)
            
    elif option == 0:
        print("Bye")
    else:
        print("Invalid input")

ATM()








