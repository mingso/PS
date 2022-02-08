import sys

n = int(sys.stdin.readline())
suyeol = list(map(int, sys.stdin.readline().split()))

d = [0] * n

for i in range(n):
    for j in range(i):
        if suyeol[i] > suyeol[j] and d[i] < d[j]:
            d[i] = d[j]
    d[i] += 1

print(max(d))