#PROBLEM #005

"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

a=1
i=1
while i < 20:
    if a%i !=0:
        a+=1
        i=1
    else:
        i+=1
print(a)          
        
        