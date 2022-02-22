import sys
from itertools import combinations

while True:
    nums = list(map(int, sys.stdin.readline().split()))

    if len(nums) == 1:
        break

    _ = nums.pop(0)
    nums.sort()

    res = list(combinations(nums, 6))

    for r in res:
        print(' '.join(map(str, r)))
    print()