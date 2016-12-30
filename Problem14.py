"""
Problem 14

The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.

Takes a while but got answer of 525 which has 837799 sequences
"""
def isEven(x):
    return int(x/2)
def isOdd(x):
    return int((3*x)+1)
def nextSequence(x):
    if (x % 2 == 0):
        return isEven(x)
    else:
        return isOdd(x)
"""
#test
num = 13
counter = 1
while (num >1):
    num = nextSequence(num)
    print(num)
    counter += 1
print(counter)
"""

tempCount = 0
tempNum = 0
for x in range(999999, 1, -1):      #starts from 999999 until it reaces 1
    counter = 1
    if (x == 1):break
    num = x
    while (num > 1):        #does the calculations and has a counter
        num = nextSequence(num)
        counter += 1
    if (counter > tempCount):       #stores the number with the largest sequence
        tempCount = counter
        tempNum = x

print(tempCount)
print(tempNum)