import copy
import sys
from collections import deque

def BFS():
    queue = deque([puzzle])
    dist[puzzle] = 0

    while queue:
        pzzl = queue.popleft()

        if pzzl == answer:
            return dist[pzzl]

        i = pzzl.find('0')
        x, y = i // 3, i % 3

        for k in range(4):
            X = x + dx[k]
            Y = y + dy[k]
            if 0 <= X < 3 and 0 <= Y < 3:
                pzz = list(pzzl)
                pzz[x*3 + y] = pzz[X*3 + Y]
                pzz[X*3 + Y] = '0'
                pzz = ''.join(pzz)
                if not dist.get(pzz) or dist[pzz] > dist[pzzl] + 1:
                    dist[pzz] = dist[pzzl] + 1
                    queue.append(pzz)

    return -1


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

puzzle = ''.join(sum([list(sys.stdin.readline().split()) for _ in range(3)], []))
answer = '123456780'
dist = dict()

print(BFS())