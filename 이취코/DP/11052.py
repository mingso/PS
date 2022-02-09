import sys

n = int(sys.stdin.readline())
d = [0] * (n+1)
cards = [0] + list(map(int, sys.stdin.readline().split()))

d[1] = cards[1]

for i in range(2, n+1):
    for j in range(1, i+1):
        if d[i] < d[i-j] + cards[j]:
            d[i] = d[i-j] + cards[j]

print(d[n])