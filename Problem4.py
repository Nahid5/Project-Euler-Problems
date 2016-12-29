"""
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
def palindrome(num):
    return str(num) == str(num)[::-1]       #extended slices to reverse the string and checks if they are the same

for x in range (999, 0, -1):       #backwards from 999 to 1
    for y in range (999, 0, -1):
        for z in range (999, 0, -1):
            if (palindrome(x*y*z) == True):
                print(x)
                print(y)
                print(z)
                break
        if (palindrome(x * y * z) == True):
            break
    if (palindrome(x * y * z) == True):
        break