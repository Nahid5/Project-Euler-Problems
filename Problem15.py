"""
Problem 15

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
############There's an image here https://projecteuler.net/problem=15###############################
How many such routes are there through a 20×20 grid?
"""
import math
#https://www.youtube.com/watch?v=M8BYckxI8_U
#a video that helped

def nCr(n,r):       #this works only on full grids
    ans = math.factorial(n)/(math.factorial(r)*(math.factorial(n-r)))
    return ans

x = 20      #horizontal length
y = 20      #verticle length
print("The routes through a 20x20 grid is: " + str(nCr(x+y, y)))