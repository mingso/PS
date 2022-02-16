import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

answer = 0
for i in range(n-1, -1, -1):
    for j in range(n):
        if j >= i:
            break
        if nums[j] > nums[j+1]:
            temp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = temp
            answer += 1

print(nums)
