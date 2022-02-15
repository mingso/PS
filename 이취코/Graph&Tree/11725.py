import sys
sys.setrecursionlimit(10**9)

def DFS(parent, start):
    for i in tree[start]:
        if parent[i] == 0:
            parent[i] = start
            DFS(parent, i)

n = int(sys.stdin.readline())

tree = [[] for _ in range(n+1)]
parent = [0 for _ in range(n+1)]

for _ in range(n-1):
    n1, n2 = map(int, sys.stdin.readline().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

DFS(parent, 1)

for i in range(2, n+1):
    print(parent[i])