"""
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

Takes a while for large numbers
"""
below = 10
sum = 0
for x in range(2, below+1):
    incounter = 0
    for y in range (2, x+1):
        if (x%y == 0):
            incounter += 1

    if (incounter == 1):
        sum += x

print (sum)