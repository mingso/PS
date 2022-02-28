import sys
from itertools import combinations

n, s = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

answer = 0
for i in range(1, n+1):
    for comb in list(combinations(nums, i)):
        if sum(comb) == s:
            answer += 1

print(answer)