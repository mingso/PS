n, c = map(int, input().split())

data = []
for _ in range(n):
    data.append(int(input()))
data.sort()

start = data[1] - data[0]
end = data[-1] - data[0]
result = 0

while start <= end :
    mid = (start + end) // 2
    value = data[0]
    count = 1
    # 앞에서부터 공유기 설치
    for i in range(1, n):
        if data[i] >= value + mid:
            value = data[i]
            count += 1

    if count >= c: # c개 이상이 가능한 경우 거리 증가
        start = mid + 1
        result = mid # 최적값 저장
    else: # c개 이상의 공유기를 설치할 수 없는 경우, 거리 감소.
        end = mid -1

print(result)
