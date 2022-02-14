import sys

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

h, w = map(int, sys.stdin.readline().split())

maps = []
queue = [(0, 0)]

for i in range(h):
    maps.append(list(sys.stdin.readline().rstrip()))

while queue:
    x, y = queue[0][0], queue[0][1]
    del queue[0]

    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]

        if 0 <= X < h and 0 <= Y < w and maps[X][Y] == '1':
            queue.append((X, Y))
            maps[X][Y] = int(maps[x][y]) + 1

print(maps[h-1][w-1])