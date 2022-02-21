import sys

broken = set()

c = list(sys.stdin.readline().rstrip())
channel = int(''.join(map(str, c)))
m = int(sys.stdin.readline())

if m:
    broken = set(sys.stdin.readline().split())

answer = abs(100 - channel)

if answer != 0:
    for num in range(1000001):
        for n in str(num):
            if n in broken:
                break
        else:
            answer = min(answer, len(str(num)) + abs(channel - num))

print(answer)