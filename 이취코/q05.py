n, m = map(int, input().split())

bowling = list(map(int, input().split()))

bowling.sort()

count = 0
for i in range(len(bowling)):
    for j in range(i+1, len(bowling)):
        if bowling[i] != bowling[j]:
            count += 1

print(count)