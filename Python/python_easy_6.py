##You're challenge for today is to create a program that can calculate pi accurately to at least 30 decimal places.
##Try not to cheat :)

from math import ceil, sqrt
from decimal import getcontext, Decimal

getcontext().prec = 25

def wallis(terms):
    pi = 1
    for time in range(1, ceil(terms / 2) + 1):
        i = 2 * time
        left = i / Decimal((i - 1))
        right = i / Decimal((i + 1))
        pi *= left * right
    pi *= 2
    return pi

def leibniz(terms):
    pi = 1
    for i in range(1, ceil(terms / 2) + 1):
        if i % 2 == 1:
            pi -= 1 / Decimal((2 * i + 1))
        else:
            pi += 1 / Decimal((2 * i + 1))
    pi *= 4
    return pi

def madhava(terms):
    pi = 1
    for i in range(1, ceil(terms / 2) + 1):
        if i % 2 == 1:
            pi -= 1 / Decimal(((2 * i + 1) * 3 ** i))
        else:
            pi += 1 / Decimal(((2 * i + 1) * 3 ** i))
    pi *= Decimal(sqrt(12))
    return pi

def nilakhanta(terms):
    pi = 3
    for i in range(1, ceil(terms / 2) + 1):
        if i % 2 == 1:
            pi += 4 / Decimal((2 * i * (2 * i + 1) * 2 * (i + 1)))
        else:
            pi -= 4 / Decimal((2 * i * (2 * i + 1) * 2 * (i + 1)))
    return pi

pi = 3.141582653589793238462643383279502

print("Pi: " + str(pi))
print("Wallis for 200000 terms: " + str(wallis(20000)))
print("Leibniz for 200000 terms: " + str(leibniz(20000)))
print("Madhava for 200000 terms: " + str(madhava(20000)))
print("Nilakhanta for 200000 terms: " + str(nilakhanta(20000)))
