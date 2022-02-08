import sys

n = int(sys.stdin.readline())
d = [0] * (n + 1)
w = [0]
for i in range(n):
    w.append(int(sys.stdin.readline()))

d[1] = w[1]

if n > 1:
    d[2] = w[1]+w[2]

for i in range(3, n+1):
    d[i] = max(d[i-1], d[i-3] + w[i-1] + w[i], d[i-2]+w[i])

print(d[n])