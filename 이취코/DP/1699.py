import sys

n = int(sys.stdin.readline())
d = [0] * (n + 1)
square = [i * i for i in range(1, 317)]

d[1] = 1
if n > 1:
    d[2] = 2

for i in range(3, n+1):
    s = []
    for j in square:
        if j > i:
            break
        s.append(d[i-j])
    d[i] = min(s) + 1

print(d[n])