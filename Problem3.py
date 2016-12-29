"""
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
theNumber = 600851475143
for x in range(2,theNumber+1):        #the range should start from 2 to not include 1
    counter = 0
    if (theNumber % x == 0):        #checks if a number is a factor
        for y in range (1, x+1):        #checks if the number has more than 2 factors
            if (x % y == 0):
                counter += 1
    if (counter == 2):
        print (x)
