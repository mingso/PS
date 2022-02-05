n, m = map(int, input().split())
cards = []

res = []

for i in range(n):
    cards.append([])
    row = list(map(int, input().split()))
    res.append(min(cards[i]))

print(max(res))