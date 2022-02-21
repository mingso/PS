import sys
import math
from collections import deque

def isPrimeNumber(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def bfs():
    q = deque()
    q.append(before)

    while q:
        x = q.popleft()
        if x == after:
            print(dist[x])
            break
        nums = list(str(x))

        for i in range(1, 10):
            num = int(str(i) + ''.join(map(str, nums[1:])))
            if num != x and num in primes and not dist[num]:
                dist[num] = dist[x] + 1
                q.append(num)

        for i in range(0, 10):
            num = int(nums[0] + str(i) + ''.join(map(str, nums[2:])))
            if num != x and num in primes and not dist[num]:
                dist[num] = dist[x] + 1
                q.append(num)

        for i in range(0, 10):
            num = int(''.join(map(str, nums[0:2])) + str(i) + nums[3])
            if num != x and num in primes and not dist[num]:
                dist[num] = dist[x] + 1
                q.append(num)

        for i in range(0, 10):
            num = int(''.join(map(str, nums[:3])) + str(i))
            if num != x and num in primes and not dist[num]:
                dist[num] = dist[x] + 1
                q.append(num)

primes = []
t = int(sys.stdin.readline())

for i in range(1009, 10000, 2):
    if isPrimeNumber(i):
        primes.append(i)

for _ in range(t):
    dist = [0] * 10001
    before, after = map(int, sys.stdin.readline().split())
    bfs()
