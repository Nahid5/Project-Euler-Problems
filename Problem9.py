'''
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

breakout = False

for c in range(2, 1000):
    for a in range(1, c):
        b = 1000 - c - a
        if a**2 + b**2 == c**2:
            print(a)
            print(b)
            print(c)
            print(a*b*c)
            breakout = True
            break
    if (breakout == True):
        break