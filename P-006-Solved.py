# PROBLEM #006

"""The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

sq_sum=[]
sum_sq=[]

sq_sum= [x**2 for x in range(101)]
sum_sq= [x+1 for x in range(100)]

print((sum(sum_sq)**2)-sum(sq_sum))