import sys

sys.setrecursionlimit(10000)

def DFS(graph, root, visited):
    visited[root] = True
    for i in graph[root]:
        if not visited[i-1]:
            DFS(graph, i-1, visited)

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    graph = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    nodes = list(map(int, sys.stdin.readline().split()))

    for i in range(0, n):
        graph[i].append(nodes[i])

    answer = 0
    for i in range(0, n):
        if visited[i] == False:
            answer += 1
            DFS(graph, i, visited)
    print(answer)