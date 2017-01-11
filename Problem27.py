"""
Problem 27

It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41
is clearly divisible by 41.
The incredible formula n2−79n+1601
was discovered, which produces 80 primes for the consecutive values 0≤n≤79
. The product of the coefficients, −79 and 1601, is −126479.
Considering quadratics of the form:
    n2+an+b
, where |a|<1000 and |b|≤1000
where |n|
is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a
and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
"""
import math
import time

start = time.time()

#checks if a number is a prime number or not
def isPrime(num):
# http://stackoverflow.com/questions/5811151/why-do-we-check-up-to-the-square-root-of-a-prime-number-to-determine-if-it-is-pr
    for x in range(2, math.ceil(math.sqrt(num))):
        if (num % x == 0): return False
    return True

#doen with brute force
higX = 0
higY = 0
max_n = 0       #max counter for number of primes
for x in range(-999,1000):          #-999 to 999 since excludes 1000
    for y in range(-1000,1001):     #-1000 to 1000 since includes 1000
        n = 0
        counter = 0
        while True:
            if (isPrime(abs((n**2) + (x*n) + y ))): counter += 1
            else: break
            n += 1
        if (counter > max_n):           #stores the info for the equation with the largest primes
            max_n = counter
            highX = x
            highY = y

end = time.time() - start

print(highX)
print(highY)
print(max_n)
print(end)