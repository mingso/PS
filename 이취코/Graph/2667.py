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


n = int(sys.stdin.readline())
maps = ['0' * (n+2)]
for _ in range(n):
    temp = "0" + sys.stdin.readline().rstrip() + "0"
    maps.append(temp)
maps.append('0' * (n+2))

answer = []
for i in range(1, n+1):
    for j in range(1, n+1):
        if maps[i][j] == '1':
            res = BFS(maps, (i, j))
            if res > 0:
                answer.append(res)

answer.sort()
print(len(answer))
for a in answer:
    print(a)