"""
Problem 28

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""
#sum starts at 1 because 1 is in the center and can't go in a square pattern
sum = 1
#step is the amount increased as gouing out from the center, it always increases by 2
step = 2
#x is the starting number which is 3 and the second to frst number to start from
x = 3
while (True):
#1001*1001 gives the largest possible number in the 1001x1001 matrix
    if (x > 1001*1001):
        break
#all 4 corners of the square can be represented by the 4 sums which takes x and adds the step to get all the corners of the square
    sum += x
    sum += x + step
    sum += x + step*2
    sum += x + step*3
#this puts the value of x to the largest number in the square that it is in
    x = x + step*3
#the amount increased in each part of the square is always increased by 2
    step += 2
#add's the new step to the previous number to get the smallest number in the next square
    x += step

print(sum)