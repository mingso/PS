import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(graph, start):
    queue = deque([start])

    count = 0
    while queue:
        x, y = queue.popleft()
        if graph[x][y] == '1':
            graph[x] = graph[x][:y] + '0' + graph[x][y+1:]
            count += 1

        for i in range(4):
            if graph[x + dx[i]][y + dy[i]] == '1':
                if [(x + dx[i], y + dy[i])] not in queue:
                    queue += [(x + dx[i], y + dy[i])]

    return count

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break

    for _ in range(h):
        m = list(map(int, sys.stdin.readline().split()))
