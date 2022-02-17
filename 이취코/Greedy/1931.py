import sys

n = int(sys.stdin.readline())
meetings = []
for _ in range(n):
    meetings.append(tuple(map(int, sys.stdin.readline().split())))

meetings.sort()
meetings.sort(key=lambda x:(x[1], x[0]))

last = 0
count = 0
for i, j in meetings:
    if i >= last:
        count += 1
        last = j
print(count)