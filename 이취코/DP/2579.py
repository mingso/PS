import sys

n = int(sys.stdin.readline())
stairs = [0]
d = [0] * (n + 1)

for i in range(n):
    stairs.append(int(sys.stdin.readline()))

d[1] = stairs[1]
if n > 1:
    d[2] = stairs[1] + stairs[2]

if n > 2:
    d[3] = max(stairs[2] + stairs[3], stairs[1] + stairs[3])

for i in range(4, n+1):
    d[i] = max(d[i-3] + stairs[i-1] + stairs[i], d[i-2] + stairs[i])

print(d[n])