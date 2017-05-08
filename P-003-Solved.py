# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 21:43:35 2017

@author: Hammad
"""
"""The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?"""

def prime(num):
	# Takes in a number and returns the number back if the input is a prime or else returns 0
	counter =2
	for i in range(2,num):
		if num % i ==0:
			return 0
		elif num % i !=0:
			counter +=1
	if counter == num:
		return num

k = 2
num = 600851475143

while True:
	if num % k ==0 and prime(k)!=0:  # Test if k is a prime factor
		prime_factor = k
		num = int(num/k)  # update the number as the remainder
		k +=1
	else:
		k +=1
	if k > num:
		break
print(prime_factor)

