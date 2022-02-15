import sys
from collections import deque

def island(root):
    queue = deque([root])
    maps[root[0]][root[1]] = gID

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]

            if 0 <= X < n and 0 <= Y < n:
                if maps[X][Y] == 1:
                    queue.append((X, Y))
                    maps[X][Y] = gID
                elif maps[X][Y] == 0 and not (x, y) in ocean:
                    ocean.append((x, y))

def bridging():
    i = 0
    answer = sys.maxsize
    while ocean:
        i += 1
        length = len(ocean)
        for _ in range(length):
            x, y = ocean.popleft()
            for j in range(4):
                X = x + dx[j]
                Y = y + dy[j]

                if 0 <= X < n and 0 <= Y < n:
                    if maps[X][Y] == 0:
                        maps[X][Y] = maps[x][y]
                        ocean.append((X, Y))
                    elif maps[X][Y] < maps[x][y]:  # 다리 길이 짝수인 경우
                        answer = min(answer, (i - 1) * 2)
                    elif maps[X][Y] > maps[x][y]:  # 다리 길이 홀수인 경우
                        answer = min(answer, i * 2 - 1)
    return answer

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(sys.stdin.readline())

maps = []
ocean = deque()

for i in range(n):
    m = list(map(int, sys.stdin.readline().split()))
    maps.append(m)

gID = -1

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            island((i, j))
            gID -= 1


print(bridging())