import sys

n = int(sys.stdin.readline())
d = [[0] * 10 for _ in range(n+1)]
for i in range(0, 10):
    d[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        d[i][j] = sum(d[i-1][j:])

print(sum(d[n]) % 10007)