import sys
import math

x = sys.stdin.readline().rstrip()

while len(x) % 3 != 0:
    x = '0' + x

answer = ""
for i in range(len(x), 0, -3):
    n = x[i-3:i]
    oct = 0
    for j in range(3):
        oct += int(n[j]) * math.pow(2, 2-j)
    answer = str(int(oct)) + answer

print(answer)