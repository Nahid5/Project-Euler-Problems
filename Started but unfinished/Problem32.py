"""
Problem 32

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""
import time

start = time.time()

def isPandigit(num):
    num = sorted(num)
    '''
    if ((num == ['1','2','3'] and len(num) == 3) or (num == ['1','2','3','4'] and len(num) == 4)
        or (num == ['1','2','3','4','5'] and len(num) == 5) or (num == ['1','2','3','4','5','6'] and len(num) == 6)
        or (num == ['1', '2','3','4','5','6','7'] and len(num) == 7 ) or (num == ['1','2','3','4','5','6','7','8'] and len(num) == 8)
        or (num == ['1','2','3','4','5','6','7','8','9'] and len(num) == 9)):
        return True
    '''
    if (num == ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
        return True
    else: return False


total = 0
for x in range (1, 9999):
    for y in range (10000, x, -1):
        if (x*y > 987654321 or len(str(x) + str(y)) > 9 or len(str(x)) + len(str(y)) > 5): break
        ans = x*y
        strin = str(x) + str(y) + str(ans)
        if (isPandigit(strin)):
            total += ans

end = time.time() - start

print (total)
print (end)