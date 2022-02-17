import sys

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
coins.sort(reverse=True)

count = 0

for coin in coins:
    count += k // coin
    k %= coin

print(count)