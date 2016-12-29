"""
Problem 6

The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

square = 0
squareSum = 0

for x in range (0, 101):
    squareSum += x
    square += x**2      #squares the numbers

squareSum = squareSum**2
print ("Square = " + str(square))
print ("Square Sum = " + str(squareSum))
print (squareSum-square)