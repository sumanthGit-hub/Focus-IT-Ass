# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 23:15:25 2020

@author: sumant
"""

# Discount Calculator App
i=1
amount=None
dist = None
items={}
print("If items over enter 0(zero) to exit.")
while True:
    items[f'item{i}'] = int(input("Enter Purchases Item Amount: "))
    if items[f'item{i}'] == 0:
        break
    i+=1

total=sum(items.values())

if total <= 1000:
    dist = 0
    amount=0
elif total >=1001 and total <=2000:
    dist = 10
    amount=total*0.10
elif total >= 2001 and total <= 3000:
    dist = 20
    amount=total*0.20
elif total >= 3001:
    dist = 25
    amount=total*0.25
else:
    print("Enter Valid Details")
    
pay=total-amount
print("Purchases amount: ",items)
print("Discount        : ",dist,"%")
print("Total Bill      : ",total)
print("Discount Bill   : ",amount)
print(f"Payment Bill : {total} - {amount} = {pay}")

