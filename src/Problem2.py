valA = 1
valB = 2
sum = 0

while True:
    if valB%2==0:
        sum += valB

    aux = valA + valB
    valA = valB
    valB = aux

    if valB>=4000000:
        break

print(sum)
