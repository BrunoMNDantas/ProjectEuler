def isPolindrome(num):
    num = str(num)

    stopIdx = int(len(num)/2)

    for i in range(0, int(len(num)/2)):
        if num[i] != num[len(num)-i-1]:
            return False

    return True

def findMaxMultiplicationPolindrome():
    largest = 0

    for i in reversed(range(100, 1000)):
        for j in reversed(range(100, 1000)):
            if i*j <= largest:
                break
            if isPolindrome(i*j):
                largest = i*j

    return largest



print(findMaxMultiplicationPolindrome())
