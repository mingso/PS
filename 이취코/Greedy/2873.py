import sys

# def bfs():


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]



r, c = map(int, sys.stdin.readline().split())
maps = []
for _ in range(r):
    maps.append(list(map(int, sys.stdin.readline().split())))

print(maps)
