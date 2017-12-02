def isDivisible(num, frm, to):
    for i in range(frm, to+1):
        if num % i != 0:
            return False

    return True


i = 2520
while True:
    if isDivisible(i, 1, 20):
        print(i)
        break
    i += 2520
