# PROBLEM 007

"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?"""

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




counter = 0 # counter for the number of primes reached
k = 2 # initilazing the first number to test
while True:
	if counter > 10000:
		print(k-1)
		break
	elif prime(k) !=0:
		counter +=1
		k +=1
	else:
		k +=1
