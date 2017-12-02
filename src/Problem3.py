from math import sqrt

def factor(num):
    for i in range(2, num+1):
        if num%i==0:
            return sorted([i] + factor(int(num/i)))

    return []

def isPrime(num):
    for i in range(2,int(sqrt(num))+1):
        if num%i==0:
            return False

    return True



num = 600851475143
factors = factor(num)

for factor in reversed(factors):
    if isPrime(factor):
        print(factor)
        break
