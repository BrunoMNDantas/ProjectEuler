def sumUntil(num):
    return 1 if num == 1 else num+sumUntil(num-1)

def sumSquaresUntil(num):
    return 1 if num == 1 else num**2+sumSquaresUntil(num-1) 

print(sumUntil(100)**2 - sumSquaresUntil(100))
