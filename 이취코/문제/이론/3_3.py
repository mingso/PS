n, k = map(int, input().split())

count = 0
while n != 1 :
    if n % k == 0 :
        n /= k
        count += 1
    else :
        res = int(n % k)
        n -= res
        count += res

print(count)