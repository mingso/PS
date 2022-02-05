import heapq
INF = int(1e9)

n, m = map(int, input().split())
li = []

# n -> k -> x

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

start = 1

graph = [[] for i in range(n+1)]

distance = [INF] * (n+1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append((y, 1))


x, k = map(int, input().split())

ans = 0
dijkstra(start)

if distance[k] == INF :
    ans = -1
else :
    ans += distance[k]

    dijkstra(k)
    if distance[x] == INF :
        ans = -1
    else :
        ans += distance[x]

print(ans)