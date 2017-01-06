"""
Problem 24

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import time
from itertools import permutations


start = time.time()
theNumbers = "0123456789"
perms = [''.join(p) for p in permutations(theNumbers)]      #used the permutation itertools to find all permutations
perms.sort()        #sorted them numerically
print("the one millions permutation is " + perms[999999])       #printed the 1000000

elapsed = time.time() - start
print("seconds " + str(elapsed))