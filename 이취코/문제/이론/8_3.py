n = int(input())

# (n, 2)를 1x2, 2x1, 2x2로 채움.

# 1*2 -> 1
# 2*2 를 채우는 방법 -> 3

d = [0] * 1001

d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i-1] + 2 * d[i-2]) % 796796

print(d[n])