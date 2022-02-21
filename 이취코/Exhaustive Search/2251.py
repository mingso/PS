import sys
from collections import deque

answer = set()
A, B, C = map(int, sys.stdin.readline().split())

allCases = set()
queue = deque()
queue.append((0, 0, C))

while True:
    try:
        thisCase = queue.popleft()
    except:
        break
    a, b, c = thisCase[0], thisCase[1], thisCase[2]
    if a == 0:
        answer.add(c)
    allCases.add(thisCase)

    nextCases = []
    if a < A and c > 0:
        nextCases.append((min(A, a + c), b, max(c - (A-a), 0)))

    if b < B and c > 0:
        nextCases.append((a,  min(B, b + c), max(c - (B-b), 0)))

    if a > 0:
        nextCases.append((max(a - (C-c), 0), b, min(C, a + c)))
        nextCases.append((max(a - (B-b), 0), min(B, a + b), c))

    if b > 0:
        nextCases.append((a, max(b - (C-c), 0), min(C, b + c)))
        nextCases.append((min(A, b + a), max(b - (A-a), 0), c))

    for nextCase in nextCases:
        if nextCase not in allCases:
            queue.append(nextCase)

answer = list(answer)
answer.sort()

print(' '.join(map(str, answer)))