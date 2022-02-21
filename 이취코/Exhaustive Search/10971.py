import sys

n, k = map(int, sys.stdin.readline().split())

answer = 0

if answer != 0:
    for num in range(1000001):
        for n in str(num):
            if n in broken:
                break
        else:
            answer = min(answer, len(str(num)) + abs(channel - num))