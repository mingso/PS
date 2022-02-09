import sys

n, k = map(int, sys.stdin.readline().split())
d = [[0] * (n + 1) for i in range(k + 1)]

if k <= 1:
    for i in range(n + 1):
        d[1][i] = 1
else:
    for i in range(n + 1):
        d[1][i] = 1
        d[2][i] = i+1

for i in range(2, k+1):
    d[i][1] = i
    for j in range(2, n+1):
        d[i][j] = d[i][j-1] + d[i-1][j]

print(d[k][n] % 1000000000)


# import math
# n, k = map(int,input().split())
# print(math.comb(n + k - 1, n) % 10 ** 9)