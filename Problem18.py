"""
Problem 18

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
3
7 4
2 4 6
8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom of the triangle below:
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
"""
import numpy as np


lines = []
with open("problem18.txt") as myFile:
    lines = [line.split() for line in myFile]       #max of 15 lines

for x in lines:
    while (len(x) != len(lines)):
        x.append('00')        #adds a 00 so every list has the same amout of elements
    #print(x)   used to check the elements in the list
data = np.reshape(lines, (-1, len(lines)))        #convert from 1d array to 2d

possiblePaths = 2**(len(lines)-1)

for x in range(len(data)-2, -1,-1):     #starts at the second to last row
    for y in range(0, len(data[x])):    #from 0 to the last element on the column
        if (data[x][y] != "00"):       #checks current place
            temp1 = int(lines[x][y]) + int(data[x+1][y])        #adds the curent number to bottom number
            temp2 = int(lines[x][y]) + int(data[x+1][y+1])      #adds the current number to bottom right
            if (temp1 > temp2):
                data[x][y] = str(temp1)     #replace current number if bototm number is larger
            else:
                data[x][y] = str(temp2)     #replace current number if bottom right is larger
print("The Largest possible number is: " + data[0][0])      #position [0][0] will always hold the largest number in the pyramid
