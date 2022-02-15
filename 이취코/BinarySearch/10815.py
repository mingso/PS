import sys

def binarySearch(num):
    start, end = 0, n-1
    while start <= end:
        mid = (start + end) // 2
        if hadCards[mid] == num:
            return 1
        elif hadCards[mid] > num:
            end = mid - 1
        elif hadCards[mid] < num:
            start = mid + 1
    return 0


n = int(sys.stdin.readline())
hadCards = list(map(int, sys.stdin.readline().split()))
hadCards.sort()

m = int(sys.stdin.readline())
allCards = list(map(int, sys.stdin.readline().split()))

for card in allCards:
    if binarySearch(card) == 1:
        print(1, end=' ')
    else:
        print(0, end=' ')