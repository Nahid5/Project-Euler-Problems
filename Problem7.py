"""
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?

Takes too logn to calculate
"""
import math

numberToGer = 10001     #change to get the specific prime number
counter = 0

for x in range (2, 9999999):
    inCount = 0
    for y in range (2,x+1):
        if (x % y == 0):
            inCount += 1
            print (inCount)


    if (inCount == 1):
        counter += 1
        if (counter == numberToGer):
            print (x)
            break