#PROBLEM # 16

"""2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?"""


num = 2**1000
num = str(num)
sum_num = 0

for i in range(len(num)):
	sum_num += int(num[i])

print(sum_num)