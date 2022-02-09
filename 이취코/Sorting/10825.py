import sys

n = int(sys.stdin.readline())
students = []

for _ in range(n):
    name, korean, english, math = sys.stdin.readline().split()
    korean, english, math = int(korean), int(english), int(math)
    students.append((name, korean, english, math))

answer = sorted(students, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for ans in answer:
    print(ans[0])