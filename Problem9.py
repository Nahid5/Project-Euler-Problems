'''
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
import random
"""
a+b+c = 1000
a < sidesTotal/3
a < b < sidesTotal/2
c = 1000-a-b
"""
sidesTotal = 1000
a = 0
b = 0
c = 0
while(a**2+b**2 != c**2 or a+b+c != 1000):      #random if the theory is not met or the sum is not 100
    a = random.randint(1,334)       #the first number has to be lower than 100/3
    b = random.randint(335, 650)        #b is greater than a but smaller than c
    c = 1000 - a - b        #using the equation

print(a)
print(b)
print(c)