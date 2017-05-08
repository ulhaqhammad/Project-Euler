#PROBLEM #056

"""A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.Considering natural numbers of the form, a**b, where a, b < 100, what is the maximum digital sum?"""

def sum_digits(num):
	# Takes in a number and returns the sum of the digits
	digit_sum =0
	for i in str(num):
		digit_sum += int(i)
	return digit_sum


highest_sum = 0
for a in range(1,100):
	for b in range(1,100):
		power = a**b
		new_sum = sum_digits(power)
		if new_sum > highest_sum:
			highest_sum = new_sum  # update highest sum
print(highest_sum)