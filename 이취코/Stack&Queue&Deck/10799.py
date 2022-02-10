import sys

parenthesis = sys.stdin.readline().rstrip()
stack = 0
answer = 0
for i in range(len(parenthesis)):
    if parenthesis[i:i+2] == "((":
        stack += 1
    elif parenthesis[i:i+2] == "()":
        answer += stack
    elif parenthesis[i:i+2] == "))":
        stack -= 1
        answer += 1

print(answer)