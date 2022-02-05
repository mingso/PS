n = int(input())

data = list(map(int, input().split()))

answer = 0
for i in range(0, n-1):
    if data[i+1] > data[i]:
        answer += 1

print(answer)