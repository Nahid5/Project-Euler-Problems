"""
Problem 31

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:
    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""
import time

start = time.time()
ways = 0
#checks one by one if the number's combine to make 200
#teh numbers increase b/c having large numbers would slow down and 200*2 = 400, so keeping low numbers is safe and faster
for a in range(0,3):
    for b in range(0, 3):
        for c in range(0, 5):
            for d in range(0, 20):
                for e in range(0, 30):
                    for f in range(0, 50):
                        for g in range(0, 150):
                            for h in range(0, 201):
                                if (h + 2 * g + 5 * f + 10 * e + 20 * d + 50 * c + 100 * b + 200 * a > 200):break
                                if (h + 2*g + 5*f + 10*e + 20*d + 50*c + 100*b + 200*a == 200):
                                    ways += 1

end = time.time() - start
#answer is 73682 and takes about 162 seconds
print(end)
print(ways)