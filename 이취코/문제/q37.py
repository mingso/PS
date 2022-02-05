n = int(input())
m = int(input())

village = [[1e9] * n for i in range(n)]
for i in range(n):
    village[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    a = a-1
    b = b-1
    village[a][b] = min(village[a][b], c)

for k in range(n):
    for a in range(n):
        for b in range(n):
            village[a][b] = min(village[a][b], village[a][k] + village[k][b])


print(village)