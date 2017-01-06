"""
Problem 26

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""
import time


start = time.time()
#checks if the decimal is terminating or not (1/x)
def isTer(x):
    while (x > 1):
        if (x % 2 == 0): x = x/2
        elif (x % 5 == 0): x = x/5
        else: return False
    return True
"""
1/7
7  goes into 1, 0 times, move decimal (0.???)
7 goes into 10, 1 time, remainder is 3, move decimal(0.1???)
7 goes into 30, 4 times, remainder is 2, move decimal (0.14???)
7 goes into 20, 2 times, remainder is 6, move decimal (0.142???)
7 goes into 60, 8 times, remainder is 4, move decimal (0.1428???)
7 goes into 40, 5 times, remainder is 5, move decimal (0.14285???)
7 goes into 50, 7 times, remainder is 1, move decimal (0.142857???)
7 goes into 10, 1 times, remainder is 3, .......
"""
def getDecimals(num,den):       #numerator, denominator
    listOfDec = []
    listOfDec.append(str(num) + "/" + str(den))                 #the fraction stored in the list
    num = 10 * (int(num % den))                                 #the next gumerator is generated
    while True:
        if ((str(num) + "/" + str(den)) in listOfDec or num == 0):break         #stop if the numerator + denominator combo is already in the list
        else:
            listOfDec.append(str(num) + "/" + str(den))
            num = 10 * (int(num % den))
    return len(listOfDec) - 1                                    #to compinsate for the first 0 in everything

largest = 0
larNum = 0
for x in range (2, 1001):
    if (isTer(x) == False):
        temp = getDecimals(1, x)
        if (temp > largest):
            largest = temp
            larNum = x

print("The largest repeating fraction has: "+ str(largest))
print("The fraction that has this many is: " + "1/" + str(larNum))


elapsed = time.time() - start
print("seconds " + str(elapsed))