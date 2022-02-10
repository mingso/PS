import sys

t = int(sys.stdin.readline())

for _ in range(t):
    stack = []
    parenthesis = sys.stdin.readline().rstrip()
    answer = "YES"

    for paren in parenthesis:
        if paren == '(':
            stack.append('(')
        else:
            try:
                stack.pop()
            except:
                answer = "NO"
                break

    if len(stack) != 0:
        answer = "NO"

    print(answer)
