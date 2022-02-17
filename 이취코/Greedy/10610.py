import sys

nums = list(sys.stdin.readline().rstrip())

if min(nums) != '0':
    print(-1)
    exit(0)

nums.sort(reverse=True)
maxNum = int(''.join(map(str, nums)))

if maxNum % 3 == 0:
    print(maxNum)
else:
    print(-1)