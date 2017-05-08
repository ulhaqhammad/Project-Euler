#PROBLEM 010:

"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million."""

def primes(n):
	sum_primes =0
	sieve = [True] * (n+1)
	for p in range(2, n+1):
		if (sieve[p]):
			sum_primes += p
			for i in range(p, n+1, p):
				sieve[i] = False
	print(sum_primes)