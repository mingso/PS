n, m, k = map(int, input().split())

num = input().split()
num.sort(reverse=True)

sum = 0
a = 0
# for i in range(m):
    # a += 1
    # if a <= k :
    #     sum += int(num[0])
    # else:
    #     sum += int(num[1])
    #     a = 0

tmp = int(num[0]) * k + int(num[1])
sum += tmp * (m // (k+1))
sum += int(num[0]) * (m % (k+1))

print(sum)