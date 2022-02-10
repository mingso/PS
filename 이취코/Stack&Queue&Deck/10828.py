import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    op = sys.stdin.readline().split()

    if op[0] == "push":
        stack.append(int(op[1]))
    elif op[0] == "pop":
        try:
            print(stack.pop())
        except:
            print("-1")
    elif op[0] == "size":
        print(len(stack))
    elif op[0] == "empty":
        print("1" if len(stack) == 0 else "0")
    elif op[0] == "top":
        try:
            print(stack[-1])
        except:
            print("-1")