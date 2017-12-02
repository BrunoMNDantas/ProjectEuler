def isPythagoreanTriplet(a,b,c):
    return ((a**2) + (b**2)) == (c**2)

def getTriplet():
    for a in range(1,1000):

        for b in range(a,1000):
            if a+b > 1000:
                break

            for c in range(b,1000):
                if a+b+c > 1000:
                    break

                if a+b+c == 1000 and isPythagoreanTriplet(a,b,c):
                    return [a,b,c]



triplet = getTriplet()
print(triplet[0]*triplet[1]*triplet[2])
