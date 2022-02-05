n, m = map(int, input().split())

rice_cake = list(map(int, input().split()))

sum = 0
h = max(rice_cake) - 1

while sum < m:
    tmp_sum = 0
    for i in rice_cake:
        tmp_sum += i - h if i-h > 0 else 0

    print(tmp_sum, m)
    if tmp_sum <= m :
        sum = tmp_sum

    h -= 1

print(h+1)