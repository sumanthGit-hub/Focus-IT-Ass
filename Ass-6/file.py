# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 22:01:55 2020

@author: sumant
"""

################## File Handling #########################################

with open("file1.txt",'w') as f:
    f.write("Python is easy to learn")
    
with open("file1.txt",'r') as r:
    line=r.readlines()
    print("Lines       :",len(line))
    words=line[0].split(" ")
    print("Words       :",len(words))
    count=[x for x in line[0] if x != " "]
    print("Charcters   :",len(count))
