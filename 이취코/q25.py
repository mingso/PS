def solution(N, stages):
    answer = []

    sol = [0] * (N+2)
    unsol = [0] * (N+2)
    for i in stages:
        for j in range(1, i+1):
            unsol[j] += 1
            sol[j] += 1

        sol[i] -= 1

    ans = []
    for i in range(1, len(sol)-1):
        ans.append((i, sol[i]/unsol[i]))

    ans.sort(key=lambda x:x[1])

    for (i, n) in ans:
        answer.append(i)

    return answer

print(solution(4, [4, 4, 4, 4, 4]))