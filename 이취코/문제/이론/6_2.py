n = int(input())

students = []
for i in range (n):
    name, score = input().split()
    score = int(score)
    students.append((name, score))

answer = sorted(students, key=lambda student: students[1])

for name, score in answer:
    print(name, end = ' ')
