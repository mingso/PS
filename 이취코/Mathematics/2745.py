import sys
import math

jinbub = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = sys.stdin.readline().split()
b = int(b)
length = len(n) - 1
answer = 0

for i in range(length, -1, -1):
    answer += jinbub.find(n[i]) * math.pow(b, (length - i))

print(int(answer))