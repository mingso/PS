import sys
from collections import deque

def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort(reverse=True)
                stack += temp
    return visited

def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort()
                queue += temp
    return visited

n, m, v = map(int, sys.stdin.readline().split())

graphList = {}
for edge in range(m):
    node1, node2 = map(int, sys.stdin.readline().split())
    if node1 not in graphList:
        graphList[node1] = [node2]
    elif node2 not in graphList[node1]:
        graphList[node1].append(node2)

    if node2 not in graphList:
        graphList[node2] = [node1]
    elif node1 not in graphList[node2]:
        graphList[node2].append(node1)

print(' '.join(map(str, DFS(graphList, v))))
print(' '.join(map(str, BFS(graphList, v))))