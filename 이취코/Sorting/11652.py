import sys

n = int(sys.stdin.readline())
cards = {}

for _ in range(n):
    m = sys.stdin.readline().strip()
    if m in cards:
        cards[m] += 1
    else:
        cards[m] = 1

answer = sorted(cards.items(), key=lambda x: (-x[1], x[0]))[0]

print(answer[0])