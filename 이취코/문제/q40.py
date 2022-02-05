n, m = map(int, input().split())

data = []
dist = [(1e9)] * n
dist[0] = 0
for _ in range(m):
    a, b = map(int, input().split())
    if a > b:
        data.append((b, a))
    else :
        data.append((a, b))

data.sort(key=lambda x:(int(x[0]), int(x[1])))

for (s, e) in data:
    s = s-1
    e = e-1
    dist[e] = min(dist[s] + 1, dist[e])

a = max(dist)
b = dist.count(a)

print(dist.index(a)+1, a, b)