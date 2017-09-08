from math import ceil, sqrt
from decimal import getcontext, Decimal

getcontext().prec = 50

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
from datetime import *
def pinalysis():
    pi = Decimal(3.14158265358979323846264338327950288419716)

    print("Pi: " + str(pi))
    
    print("Wallis for 1,000,000 terms: " + str(wallis(1000000)))
    print("Leibniz for 1,000,000 terms: " + str(leibniz(1000000)))
    print("Madhava for 10,000 terms: " + str(madhava(10000)))
    print("Nilakhanta for 1,000,000 terms: " + str(nilakhanta(1000000)))

if __name__ == "__main__":
    pinalysis()
