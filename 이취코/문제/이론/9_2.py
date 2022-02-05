import heapq
INF = int(1e9)

n, m, c = map(int, input().split()) # c== start

graph = [[] for i in range(n+1)]

distance = [INF] * (n+1)

for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

ans_num  = 0
ans_time = 0
for i in range(1, n +1):
    if distance[i] != INF:
        ans_num += 1
        ans_time = max(ans_time, distance[i])

print(ans_num-1, ans_time)