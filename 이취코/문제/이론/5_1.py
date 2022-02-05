n, m = map(int, input().split())

shape = []
for i in range(n):
    shape.append([])
    tmp = input()
    for j in tmp:
        shape[i].append(int(j))

def dfs(x, y):
    if x <= -1 or x >=n or y <= -1 or y >= m:
        return False
    if shape[x][y] == 0:
        shape[x][y] = 1

        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range (n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 11

print(result)