# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 22:02:02 2020

@author: sumant
"""

############## Plotting student progress in Bar plot #########################

import matplotlib.pyplot as plt

sub   = ["telugu","hindi","english","maths","science","social"] # Subjects
marks={}

print("Welcome....!")
print("==================")
for i in sub:
    marks[i]=int(input(f"Enter {i} marks: "))

plt.bar(marks.keys(),height=marks.values(),color="gray",width=0.6)
plt.show()