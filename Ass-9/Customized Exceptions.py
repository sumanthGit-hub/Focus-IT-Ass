# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 11:07:20 2020

@author: sumant
"""


class AttendanceShortageException(Exception):
    def __init__(self,arg):
        self.arg = arg
        
class IncomeException(Exception):
    def __init__(self,arg):
        self.arg = arg

class GPAException(Exception):
    def __init__(self,arg):
        self.arg = arg


class Details:
    
    def student(self):
        attendance = int(input("Enter Student Attendance: "))
        if attendance < 75 :
            raise AttendanceShortageException("Attendance is less")
        else:
            print("Your attendance is ",attendance)
            
    def Parentincome(self):
        income = int(input("Enter parent income: "))
        if income > 500000 :
            raise IncomeException("Parent Income is high")
        else:
            print("Parent Income is ",income)
            
    def percentage(self):
        CGPA = float(input("Enter Student CGPA: "))
        if CGPA < 7 :
            raise GPAException("CGPA is less")
        else:
            print("Your CGPA in percentage is ",CGPA*10,'%')
 
d = Details()
d.student()
d.Parentincome()
d.percentage()


