import sys

sys.setrecursionlimit(10000)

def DFS(graph, root, visited):
    visited[root] = True
    for i in graph[root]:
        if not visited[i]:
            DFS(graph, i, visited)

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
graph[0] = [0, 0]
visited = [False for _ in range(n+1)]

for _ in range(m):
    node1, node2 = map(int, sys.stdin.readline().split())
    graph[node1].append(node2)
    graph[node2].append(node1)


count = 0
for i in range(1, len(visited)):
    if not visited[i]:
        count += 1
        DFS(graph, i, visited)

print(count)