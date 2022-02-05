n, m = map(int, input().split())

data = [[int(1e9)] * n for i in range(n)]
for i in range(n):
    data[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    a = a-1
    b = b-1
    data[a][b] = 1

for k in range(n):
    for a in range(n):
        for b in range(n):
            data[a][b] = min(data[a][b], data[a][k] + data[k][b])

result = 0
for i in range(n):
    count = 0
    for j in range(n):
        if data[i][j] != int(1e9) or data[j][i] != int(1e9):
            count += 1
    if count == n:
        result += 1

print(result)