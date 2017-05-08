
# PROBLEM 004

"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers."""


def palindrome(num):
# Takes in a number a returns '1' if the number is a palindrome 
	num = str(num)
	counter =0
	if num[0] == num[-1]:
		for i in range(len(num)):
			if num[i]==num[len(num)-i-1]:
				counter +=1
			else:
				counter =0
				break
	if counter == len(num):
		return 1

L1=[]
for i in range(100,1000):
	for k in range(100,1000):
		if palindrome(i*k) ==1:
			L1.append(i*k) # list of all plindromes

print(max(L1))