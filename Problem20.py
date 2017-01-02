"""
Problem 20

n! means n × (n − 1) × ... × 3 × 2 × 1
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!
"""
import math


factorialNum = math.factorial(100)      #gets the factorial of the nu,ber

sum = 0
for x in str(factorialNum):     #converts the factorial to string and adds each character in the string as integers
    sum += int(x)

print(sum)