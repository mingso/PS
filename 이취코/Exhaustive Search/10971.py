import sys

def DFS(start, next, value, visited):
    global min_value
    if len(visited) == n:
        if maps[next][start] != 0:
            min_value = min(min_value, value + maps[next][start])
        return

    for i in range(n):
        if maps[next][i] != 0 and i != start and i not in visited:
            visited.append(i)
            if min_value > value+maps[next][i]:
                DFS(start, i, value + maps[next][i], visited)
            visited.pop()

n = int(sys.stdin.readline())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

min_value = sys.maxsize

for i in range(n):
    DFS(i, i, 0, [i])

print(min_value)