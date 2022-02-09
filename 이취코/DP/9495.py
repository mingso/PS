import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    scores = []
    for _ in range(2):
        scores.append(list(map(int, sys.stdin.readline().split())))

    if n > 1:
        scores[0][1] += scores[1][0]
        scores[1][1] += scores[0][0]

    for i in range(2, n):
        scores[0][i] += max(scores[1][i-1], scores[1][i-2])
        scores[1][i] += max(scores[0][i-1], scores[0][i-2])
    print(max(scores[0][n-1], scores[1][n-1]))