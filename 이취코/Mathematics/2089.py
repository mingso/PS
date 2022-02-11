import sys

n = int(sys.stdin.readline())

answer = ""

while n:
    if n % -2:
        answer = '1' + answer
        n = n//-2 + 1
    else:
        answer = '0' + answer
        n //= -2

print(answer if answer else "0")