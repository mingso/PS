def find_team(team, x):
    if team[x] != x:
        team[x] = find_team(team, team[x])
    return team[x]

def union_team(team, a, b):
    a = find_team(team, a)
    b = find_team(team, b)
    if a < b :
        team[b] = a
    else :
        team[a] = b

n, m = map(int, input().split())
team = [0] * (n+1)

edges = []
result = 0

for i in range(1, n+1):
    team[i] = i

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
last = 0

for edge in edges:
    cost, a, b = edge

    if find_team(team, a) != find_team(team, b):
        union_team(team,a ,b)
        result += cost
        last = cost

# 신장 트리에서 가장 큰 간선 제거
print(result - last)