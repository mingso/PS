import sys

n = int(sys.stdin.readline())
nums = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    nums.append((a, b))

answer = sorted(nums)
for ans in answer:
    print(ans[0], ans[1])