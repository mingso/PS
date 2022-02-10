import sys

n = int(sys.stdin.readline())
deque = []

for _ in range(n):
    op = sys.stdin.readline().split()

    if op[0] == "push_front":
        deque.insert(0, int(op[1]))
    elif op[0] == "push_back":
        deque.append(int(op[1]))
    elif op[0] == "pop_front":
        try:
            front = deque[0]
            deque.remove(front)
            print(front)
        except:
            print("-1")
    elif op[0] == "pop_back":
        try:
            print(deque.pop())
        except:
            print("-1")
    elif op[0] == "size":
        print(len(deque))
    elif op[0] == "empty":
        print("1" if len(deque) == 0 else "0")
    elif op[0] == "front":
        try:
            print(deque[0])
        except:
            print("-1")
    elif op[0] == "back":
        try:
            print(deque[-1])
        except:
            print("-1")