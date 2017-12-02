from math import sqrt
from itertools import count


def isPrime(num):
    for i in range(2,int(sqrt(num))+1):
        if num%i==0:
            return False

    return True



primes = 0
for i in count(2,1):
    if isPrime(i):
        primes += 1

    if primes == 10001:
        print(i)
        break
