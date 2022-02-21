import sys
from itertools import permutations

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

answer = 0
for i in list(permutations(a, n)):
    res = 0
    for j in range(n-1):
        res += abs(i[j] - i[j+1])
    answer = max(answer, res)

print(answer)