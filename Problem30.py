"""
Problem 30

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316.
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
import time


def getPow5(x):
    origX = x
    sum = 0
    while (x > 0):
#get's last number of the input number
        temp = x % 10
#removes the last number
        x = int(x/10)
#get the 5th power of the number
        sum += temp**5
#return the number only if the orignal number si the same as the sum which is all individual number to the fifth power
    if (origX == sum):
        return sum
    else:
        return 0


#9^5 = a 5 digit number
#5*9^5 = a 6 digit number, so using 999999 as an upper bound for the largest  number
start = time.time()
sumT = 0
for x in range(2,999999):
    sumT += getPow5(x)

print(sumT)
end = time.time() - start
print(end)