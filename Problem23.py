"""
Problem 23

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
#4179805 found in 826 seconds (about 14 min).  This removed numbers which adds to them selves as well so number might be a bit lower
import time
def findSum(num):       #finds divisors of the number, not including the number, but including 1
    total = 0
    for x in range(1, num+1):
        if (num % x == 0 and num != x):
            total += x
    return total

def isAbundent(num, sum):
    if (sum > num):
        return True
    else:
        return False

start = time.time()
upperLimit = 28123
lowerLimit = 12
listOfNonUppers = []
for x in range(lowerLimit, upperLimit + 1):
    listOfNonUppers.append(x)

listOfUppers = []
for x in range(0, upperLimit + 1):
    if (isAbundent(x, findSum(x)) == True):     #if the number's sum is greater than the number, it is added to the list
        listOfUppers.append(x)

for y in range(0, len(listOfUppers)):       #adds the list of abudent numbers and removes the from the list of numbers from a list of all numbers
    for z in range (0, len(listOfUppers)):
        if (listOfUppers[y] + listOfUppers[z] > upperLimit):break       #breaks if the combined number is creater than the largest number
        elif ((listOfUppers[y] + listOfUppers[z]) in listOfNonUppers):
            listOfNonUppers.remove((listOfUppers[y] + listOfUppers[z]))

elapsed = time.time() - start
print(listOfNonUppers)
print(sum(listOfNonUppers))
print("seconds " + str(elapsed))