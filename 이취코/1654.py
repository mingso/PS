import sys

k, n = map(int, sys.stdin.readline().split())
lans = []
for _ in range(k):
    lans.append(int(sys.stdin.readline()))

l = int(min(lans) / 2)
while True:
    res = 0
    for lan in lans:
         res += (lan // l)

    if res < n:
        break
    l += 1

print(l-1)