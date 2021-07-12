n = int(input())
data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i+1):
        if j == 0: # 젤 왼쪽
            up_left = 0
        else :
            up_left = data[i-1][j-1]

        if j == i: # 젤 오른쪽
            up_right = 0
        else :
            up_right = data[i-1][j]
        data[i][j] = data[i][j] + max(up_left, up_right)

print(max(data[n-1]))
