import sys

def div(a, b):
    return a / b

a, b = map(int, sys.stdin.readline().split())
print(div(a, b))