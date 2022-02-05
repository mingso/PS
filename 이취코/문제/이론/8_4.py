n, m = map(int, input().split())
d = [10001] * (m + 1)

coin = []
for i in range(n):
    coin.append(int(input()))

coin.sort()

for i in range(n):
    if i < len(coin) : d[coin[i]] = 1
    for j in range(coin[i], m+1):
        if d[j - coin[i]] != 10001:
            d[j] = min(d[j], d[j-coin[i]]+1)

print(d[m])