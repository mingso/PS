n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a의 가장 작은 값과 b의 가장 큰 값을 바꿈

for i in range (k):
    if min(a) < max(b) :
        a[a.index(min(a))], b[b.index(max(b))] = b[b.index(max(b))], a[a.index(min(a))]
    else :
        break

sum = 0
for i in a :
    sum += i

print(sum)