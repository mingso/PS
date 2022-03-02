import sys
from collections import deque

def BFS(_a):
    queue = deque()
    queue.append([_a, ""])

    answer = ""
    while queue:
        a, res = queue.popleft()
        if a == b:
            answer = res
            break

        ad = (2*a) % 10000
        if not visited[ad]:
            visited[ad] = True
            queue.append([ad, res + "D"])

        a_s = a - 1 if a-1 > 0 else 9999
        if not visited[a_s]:
            visited[a_s] = True
            queue.append([a_s, res+"S"])

        a = str(a).zfill(4)
        al = int(a[1:] + a[0])
        if not visited[al]:
            visited[al] = True
            queue.append([al, res+"L"])

        ar = int(a[3] + a[0:3])
        if not visited[ar]:
            visited[ar] = True
            queue.append([ar, res+"R"])

    return answer


T = int(sys.stdin.readline())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    visited = [False for i in range(10000)]
    print(BFS(a))
