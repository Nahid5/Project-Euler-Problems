"""
Problem 25

The Fibonacci sequence is defined by the recurrence relation:
    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:
    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144
The 12th term, F12, is the first term to contain three digits.
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
import time
start = time.time()
def fib(n):     #fast fib equation
    a = 1
    b = 0
    while (n > 1):
        a, b = a + b, a
        n = n - 1
    return a

counter = 1
num = 1
while True:
    if (len(str(fib(num))) >= 1000):break       #checks the length of the number
    else:
        num += 1
        counter += 1


print(fib(num))
print(counter)      #first 1000 digit number is the 4782 number

elapsed = time.time() - start
print("seconds " + str(elapsed))