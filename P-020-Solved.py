#PROBLEM 20

"""n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100! """

def fact(num):
	# takes in a number and returns the factorial
	factorial = 1
	for n in range(1,num+1):
		factorial *= n
	return factorial

def sum_digit(num):
	# Takes in an integer 'num' and returns the sum of all the digits in the integer
	num = str(num)
	digit_sum = 0
	for i in num:
		digit_sum += int(i)
	return digit_sum

print(sum_digit(fact(100)))