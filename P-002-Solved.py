# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 20:48:53 2017

@author: Hammad
"""
# PROBLEM #002
"""Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."""

a=[1,2]
b=[]

while True:
    if a[-1] +  a[len(a)-2] > 4000000:
        break
    else:
        a.append(a[-1]+a[len(a)-2])
for i in range(len(a)):
	if a[i]%2 == 0:
		b.append(a[i])
print (sum(b))
