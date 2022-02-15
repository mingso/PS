# cycle 찾아서 안속하는 학생 수 구하기
import sys
sys.setrecursionlimit(10000)

def DFS(x):
    global result
    visited[x] = True
    cycle.append(x)
    node = nodes[x]

    if visited[node]:
        if node in cycle:
            result += cycle[cycle.index(node):]
        return
    else:
        DFS(node)


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    nodes = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [True] + [False] * n
    result = []

    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            DFS(i)

    print(n - len(result))