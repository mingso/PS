import sys

n = int(sys.stdin.readline())
d = [0] * n

suyeol = list(map(int, sys.stdin.readline().split()))

d[0] = suyeol[0]

for i in range(1, n):
    d[i] = max(suyeol[i], d[i-1] + suyeol[i])

print(max(d))