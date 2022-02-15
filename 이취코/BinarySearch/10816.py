import sys

n = int(sys.stdin.readline())
hadCards = list(map(int, sys.stdin.readline().split()))
hadCards.sort()

_ = int(sys.stdin.readline())
allCards = list(map(int, sys.stdin.readline().split()))

hash = {}

for i in hadCards:
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1

for i in allCards:
    if i in hash:
        print(hash[i], end=' ')
    else:
        print(0, end=' ')
