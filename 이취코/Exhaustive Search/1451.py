import sys
n, m = map(int, sys.stdin.readline().split())
nums = []
for _ in range(n):
    nums.append(list(map(int, sys.stdin.readline().rstrip())))

# 111
# 222
# 333
res1 = 0
for s in range(1, n-1):
    for e in range(n-1, s, -1):
        tmp1 = 0
        for i in range(s):
            tmp1 += sum(nums[i])
        tmp2 = 0
        for i in range(s, e):
            tmp2 += sum(nums[i])
        tmp3 = 0
        for i in range(e, n):
            tmp3 += sum(nums[i])
        res1 = max(res1, tmp1*tmp2*tmp3)

# 123
# 123
# 123
res2 = 0
for s in range(1, m - 1):
    for e in range(m - 1, s, -1):
        tmp1, tmp2, tmp3 = 0, 0, 0
        for i in range(n):
            tmp1 += sum(nums[n][:s])
            tmp2 += sum(nums[n][s:e])
            tmp3 += sum(nums[n][e:])
        res2 = max(res2, tmp1*tmp2*tmp3)

# 112
# 112
# 333
res2 = 0
for i in range(1, n):
    for j in range(1, m):
        tmp2 = 0
        tmp3 = 0
        for k in range(n):
            tmp2 += sum(nums[i][:j])
            tmp3 += sum(nums[i][j:])

# 122
# 133
# 133

# 113
# 223
# 223

# 111
# 223
# 223
