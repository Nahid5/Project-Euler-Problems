"""
Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.

doing 10000 nuumbers takes a while, but smaller numbers work
"""
def findSum(num):       #finds divisors of the number, not including the number, but including 1
    total = 0
    for x in range(1, num+1):
        if (num % x == 0 and num != x):
            total += x
    return total

pairs = []
zeroToThisNumber = 1000
for x in range(0,zeroToThisNumber+1):
    if (x %2 == 0):     #amicable numbers seem to be positive
        for y in range(x + 1, zeroToThisNumber + 1):
            if (y % 2 == 0):        #amicable numbers seem to be positive
                if (x == findSum(y)
                    and y == findSum(x)):
                    pairs.append(findSum(x))
                    pairs.append(findSum(y))
                    break
print(pairs)
print(sum(pairs))