import sys
from collections import deque

def BFS(root):
    visited = [-1] * (n + 1)
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

n = int(sys.stdin.readline())

graph = {}
for i in range(1, n+1):
    graph[i] = []

for i in range(n-1):
    n1, n2, weight = map(int, sys.stdin.readline().split())
    graph[n1].append((n2, weight))
    graph[n2].append((n1, weight))

if n > 1:
    answer, node = BFS(1)
    answer, node = BFS(node)
else:
    answer = 0

print(answer)