import sys

stack1 = list(sys.stdin.readline().strip())
stack2 = []

n = int(sys.stdin.readline())

for _ in range(n):
    line = sys.stdin.readline()
    if line[0] == 'L':
        if stack1:
            stack2.append(stack1.pop())
        else:
            continue
    elif line[0] == 'D':
        if stack2:
            stack1.append(stack2.pop())
        else:
            continue
    elif line[0] == 'B':
        if stack1:
            stack1.pop()
        else:
            continue
    elif line[0] == 'P':
        stack1.append(line[2])

print(''.join(stack1 + list(reversed(stack2))))