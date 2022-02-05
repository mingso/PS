param = ["INT", "INT", "BOOL", "SHORT", "LONG"]

answer = ''
for i in param:
    if i == "BOOL":
        answer += '##'

print(answer)