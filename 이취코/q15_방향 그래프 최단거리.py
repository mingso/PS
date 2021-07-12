from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# graph[x] 에 있는거 pop 하고
# 그 안에서 또 pop 하고
# 최단거리 구함

distance = [-1] * (n+1)
distance[x] = 0

queue = deque([x])
queue.pop()
while len(queue) > 0 :
    now = queue.popleft()

    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            queue.append(next_node)

if distance.count(k) == 0:
    print('-1')
else :
    for n, dis in enumerate(distance):
        if dis == k :
            print(n)