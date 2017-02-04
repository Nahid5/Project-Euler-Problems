"""
Problem 32

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""
import time

start = time.time()

sumList = []
#checks all values.  10000 b/c 1x9999 = 9999 which is 9 digits
#stores if sum of all is a pandigit and removes duplicates with set
for x in range(1,10000):
    for y in range (x, 10001):
        list = sorted(str(x)+str(y)+str(x*y))
        if (list == ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
            sumList.append(x*y)

end = time.time() - start
print(sum(set(sumList)))
print (end)
#ans is 45228
#found in 114 seconds