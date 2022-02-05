t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    for i in range(n):
        data.append(data[:m])
        for __ in range(m):
            data.remove(data[0])

    answer = 0
    dy = [-1, 0, 1]
    index = 0
    # 처음 시작만 다 봄
    max_value = 0
    for i in range(n):
        if data[i][0] > max_value:
            max_value = data[i][0]
            index = i
    answer += max_value

    for j in range(1, m):
        max_value = 0
        next_index = 0
        for i in dy:
            if 0 <= index + i < n and data[index + i][j] > max_value:
                max_value = data[index + i][j]
                next_index = index+ i
        answer += max_value
        index = next_index

    print(answer)