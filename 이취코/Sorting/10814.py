import sys

n = int(sys.stdin.readline())
users = []

for i in range(1, n+1):
    age, name = sys.stdin.readline().split()
    age = int(age)
    users.append((i, age, name))

answer = sorted(users, key=lambda x: (x[1], x[0]))
for ans in answer:
    print(ans[1], ans[2])