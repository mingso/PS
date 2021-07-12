def find_team(team, x):
    if team[x] != x:
        team[x] = find_team(team, team[x])
    return team[x]

def union_team(team, a, b):
    a = find_team(team, a)
    b = find_team(team, b)
    if a < b :
        team[b] = a
    else :
        team[a] = b

n, m = map(int, input().split())

team = [0] * (n+1)
for i in range(1, n+1):
    team[i] = i


for i in range(m):
    op, a, b = map(int, input().split())

    if(op == 0): # 합치기
        union_team(team, a, b)

    else : # 같은 팀?
        team_a = find_team(team, a)
        team_b = find_team(team, b)
        if team_a == team_b:
            print("YES")
        else:
            print("NO")