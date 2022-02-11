import sys

def isPrime(x):
    if x == 0 or x == 1:
        return False

    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

answer = 0
for num in nums:
    if isPrime(num):
        answer += 1
print(answer)