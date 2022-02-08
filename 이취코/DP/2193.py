import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    d = [[0] * 2*n for _ in range(n+1)]

d[1][1] = 1

for i in range(2, n+1):
    for j in range(2):
        if j == 0:
            d[i][j] = d[i-1][0] + d[i-1][1]
        elif j == 1 :
            d[i][j] = d[i-1][0]

print(sum(d[n]))