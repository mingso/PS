import sys

n, c = map(int, sys.stdin.readline().split())
house = []

for _ in range(n):
    house.append(int(sys.stdin.readline()))
house.sort()

start, end = 1, house[-1] - house[0]

while start <= end:
    mid = (start + end) // 2
    cur = house[0]
    count = 1

    for i in range(1, n):
        if house[i] >= cur + mid:
            count += 1
            cur = house[i]

    if count >= c:
        start = mid + 1
    else:
        end = mid - 1

print(end)