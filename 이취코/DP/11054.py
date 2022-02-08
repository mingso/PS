import sys

n = int(sys.stdin.readline())
dp = [0] * n
dm = [0] * n
d = [0] * n
suyeol = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    for j in range(i):
        if suyeol[i] > suyeol[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

for i in range(n-1, -1 , -1):
    for j in range(n-1, i, -1):
        if suyeol[i] > suyeol[j] and dm[i] < dm[j]:
            dm[i] = dm[j]
    dm[i] += 1

for i in range(n):
    d[i] = dp[i] + dm[i] - 1

print(max(d))