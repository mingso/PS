n, x = map(int, input().split())

num = list(map(int, input().split()))

cnt = num.count(x)

if cnt == 0:
    print('-1')
else :
    print(num.count(x))