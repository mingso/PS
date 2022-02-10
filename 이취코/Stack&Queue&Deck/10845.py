import sys

n = int(sys.stdin.readline())
queue = []

for _ in range(n):
    op = sys.stdin.readline().split()

    if op[0] == "push":
        queue.insert(0, int(op[1]))
    elif op[0] == "pop":
        try:
            print(queue.pop())
        except:
            print("-1")
    elif op[0] == "size":
        print(len(queue))
    elif op[0] == "empty":
        print("1" if len(queue) == 0 else "0")
    elif op[0] == "front":
        try:
            print(queue[-1])
        except:
            print("-1")
    elif op[0] == "back":
        try:
            print(queue[0])
        except:
            print("-1")