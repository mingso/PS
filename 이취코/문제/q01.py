n = int(input())

member = list(map(int, input().split()))

member.sort(reverse = True)

team = 0
while len(member) > 0 :
    team += 1
    for i in range(member[0]):
        if len(member) > 0:
            member.pop(0)
        else :
            team -= 1
            break

print(team)