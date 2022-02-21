import sys
from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    index = 1
    answer = 0

    while q:
        x, y = q.popleft()
        isIn = False
        if index < len(word):
            for i in range(len(dx)):
                X = x + dx[i]
                Y = y + dy[i]
                if 0 <= X < m and 0 <= Y < n:
                    print(X, Y, word[index])
                    if maps[X][Y] == word[index]:
                        q.append((X, Y))
                        isIn = True
        if isIn:
            index += 1

        if index >= len(word):
            answer += 1

    return answer

n, m, k = map(int, sys.stdin.readline().split())

dx = [0] * (k * 2) + [i for i in range(1, k+1)] + [i for i in range(-1, -k-1, -1)]
dy = [i for i in range(1, k+1)] + [i for i in range(-1, -k-1, -1)] + [0] * (k * 2)


maps = [list(sys.stdin.readline().rstrip()) for _ in range(m)]
word = sys.stdin.readline().rstrip()

start = []

for i, r in enumerate(maps):
    for j, c in enumerate(r):
        if c == word[0]:
            start.append((i, j))

answer = 0

for s in start:
    answer += bfs(s)

print(answer)