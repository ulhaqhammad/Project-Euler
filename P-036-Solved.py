#PROBLEM 036

"""The decimal number, 585 = 1001001001^^2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)"""


def palindrome(num):
# Takes in a number a returns 'True' if the number is a palindrome 
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
		return True

def binary(num):
	#Takes in a number and returns the binary form of the number
	bin_num= "" 
	Flag = True
	while Flag:
		R = num % 2
		num = int(num/2)
		if R == 0 and num == 0:
			break
		bin_num +=(str(R)) # Store the the binary number in reverse order

	return int(bin_num[::-1]) # Return the binary number in the correct order



######################## Calculate sum of Palindromes ################################
sum_palindrome = 0
for i in range(1,1000001):
	if palindrome(i) == True: # check if palindrome
		if palindrome(binary(i))== True: # check if binary is also a palindrome
			sum_palindrome += i 

print(sum_palindrome)