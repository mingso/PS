INF = int(1e9)

graph = []
visited = []
distance = []


def solution(n, start, end, roads, traps):
    # n : 방번호
    # start : 시작방
    # end : 종료방
    # roads : 길
    # traps : trap있는 방

    global graph
    global visited
    global distance

    visited = [False] * (n + 1)
    distance = [INF] * (n + 1)

    for a, b, c in roads:
        trap = False
        if a in traps:
            trap = True
        graph.append((a, b, c, trap))

    graph.sort(key=lambda x: (int(x[0])))

    dijkstra(start, n, traps)

    answer = distance[n]
    return answer


def get_smallest_node(n):
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i

    return index


def dijkstra(start, n, traps):
    distance[start] = 0
    visited[start] = True
    for a, b, c, trap in graph:
        if a == start:
            distance[b] = c

    prev_node = 0
    prev_istrap = False

    for i in range(n - 1):
        now = get_smallest_node(n)
        visited[now] = True

        if prev_istrap:
            visited[prev_node] = False
            prev_node = 0
            prev_istrap = False

        if now in traps:
            prev_node = now
            prev_istrap = True
            for j, (_a, _b, _c, _trap) in enumerate(graph):
                if _a == now or _b == now:
                    graph[j] = (graph[j][1], graph[j][0], graph[j][2], graph[j][3])

        for a, b, c, trap in graph:
            if a == now:
                cost = distance[now] + c
                if visited[b] == False or (cost < distance[b] and visited == True):
                    distance[b] = cost