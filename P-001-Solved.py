# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 17:04:39 2017

@author: Hammad
"""

# PROBLEM -01 

#caluculate the sum of multiples of 3 and 5 upto 100

def sum_multiples(x,y,r):
    L1=[]
    L2=[]
    sum_list_1=0
    sum_list_2=0

    for i in range(r):
        if i % x ==0:
            L1.append(i)
    for z in range(r):
        if z % y ==0:
            L2.append(z)
    L3 = [x for x in L1 if x not in L2]
   
    sum_list_1 = sum(L2)
    sum_list_2 = sum(L3)
    print(L3)

    return sum_list_1 + sum_list_2
