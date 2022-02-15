import sys
from collections import deque

dx = [0,  0, 1, 1,  1, -1, -1, -1]
dy = [1, -1, 0, 1, -1,  0,  1, -1]

def BFS(graph, start):
    queue = deque([start])

    while queue:
        x, y = queue.popleft()
        if graph[x][y] == 1:
            graph[x][y] = 0

        for i in range(8):
            if graph[x + dx[i]][y + dy[i]] == 1:
                if [(x + dx[i], y + dy[i])] not in queue:
                    queue += [(x + dx[i], y + dy[i])]

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break

    zeroline = [0 for i in range(w + 2)]
    maps = [zeroline]
    for _ in range(h):
        m = [0] + list(map(int, sys.stdin.readline().split())) + [0]
        maps.append(m)
    maps.append(zeroline)

    count = 0
    for i in range(1, h+1):
        for j in range(1, w+1):

            if maps[i][j] == 1:
                BFS(maps, (i, j))
                count += 1
    print(count)