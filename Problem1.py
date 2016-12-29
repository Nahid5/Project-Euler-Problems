"""
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
mult5 = []
mult3 = []
#Finds all the multiple of 3 and 5
for x in range (0,1001):
    if (x % 3 == 0):
        mult3.append (x)
    if (x % 5 == 0):
        mult5.append (x)
#If an element is not in mult3 list, then it is added to mult3 from mult5
for i in mult5:
    if i not in mult3:
        mult3.append(i)
print (sum(mult3))

