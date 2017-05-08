# PROBLEM 52

"""It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits."""


Flag = True
i  = 1
counter  = 0

while Flag == True:
	num1 = str(2*i)
	num2 = str(3*i)
	num3 = str(4*i)
	num4 = str(5*i)
	num5 = str(6*i)

	if set(num2).issubset(num1) and set(num3).issubset(num1) and set(num4).issubset(num1) and set(num5).issubset(num1):
		print(i)
		Flag = False
	else:
		i += 1


