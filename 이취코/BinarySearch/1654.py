import sys

k, n = map(int, sys.stdin.readline().split())
lans = []
for _ in range(k):
    lans.append(int(sys.stdin.readline()))

start, end = 1, max(lans)

while start <= end:
    mid = (start + end) // 2
    lines = 0
    for i in lans:
        lines += i // mid

    if lines >= n:
        start = mid + 1
    else :
        end = mid - 1

print(end)