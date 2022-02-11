import sys

jinbub = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = map(int, sys.stdin.readline().split())

answer = ""

while n >= b:
    answer = jinbub[n % b] + answer
    n //= b

answer = jinbub[n] + answer

print(answer)