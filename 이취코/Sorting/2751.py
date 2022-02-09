import sys

n = int(sys.stdin.readline())
nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline()))

nums.sort()

print("\n".join(map(str, nums)))