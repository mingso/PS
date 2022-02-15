import sys

def DFS(graph, root):
    visited = []
    stack = [root]
    parent = 0

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            for node in graph[n]:
                if node in graph[parent]:
                    return "NO"

            if len(graph[n]):
                temp = list(set(graph[n]) - set(visited))
                temp.sort(reverse=True)
                stack += temp
        parent = n
    return "YES"

t = int(sys.stdin.readline())
for _ in range(t):
    v, e = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(v+1)]

    graph[0] = [0]
    for i in range(1, e+1):
        n1, n2 = map(int, sys.stdin.readline().split())
        graph[n1].append(n2)
        graph[n2].append(n1)

    print(DFS(graph, 1))
