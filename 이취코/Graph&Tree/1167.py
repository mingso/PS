import sys
from collections import deque

def BFS(root):
    visited = [-1] * (v + 1)
    queue = deque([root])
    visited[root] = 0
    maxNode = (0, 0)

    while queue:
        node = queue.popleft()
        for vertex, weight in graph[node]:
            if visited[vertex] == -1:
                queue.append(vertex)
                visited[vertex] = visited[node] + weight
                if maxNode[0] < visited[vertex]:
                    maxNode = [visited[vertex], vertex]

    return maxNode

v = int(sys.stdin.readline())

graph = {}

for i in range(v):
    info = list(map(int, sys.stdin.readline().split()))
    graph[info[0]] = []
    for j in range(1, len(info) - 1, 2):
        graph[info[0]].append((info[j], info[j+1]))

answer, node = BFS(1)
answer, node = BFS(node)

print(answer)