import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(queue, graph):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if 0 <= X < len(graph) and 0 <= Y < len(graph[0]) and graph[X][Y] == 0:
                graph[X][Y] = graph[x][y] + 1
                queue.append((X, Y))


w, h = map(int, sys.stdin.readline().split())

today = []
queue = deque([])
for i in range(h):
    m = list(map(int, sys.stdin.readline().split()))
    today.append(m)
    for j in range(w):
        if m[j] == 1:
            queue.append((i, j))

while len(queue) > 0:
    BFS(queue, today)

answer = 0
for i in today:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    answer = max(answer, max(i))

print(answer - 1)