import sys

def gcd(x, y): # 최대공약수
    if y == 0:
        return x
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)

t = int(sys.stdin.readline())

for _ in range(t):
    nums = list(map(int, sys.stdin.readline().split()))
    answer = 0
    for i in range(1, nums[0]+1):
        for j in range(i+1, len(nums)):
            answer += gcd(nums[i], nums[j])
    print(answer)
