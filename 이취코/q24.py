n = int(input())
house = list(map(int, input().split()))
house.sort()

print(house[(n-1) // 2])
# answer = [house[len(house) - 1], 1e9]
#
# for i in house:
#     dist = 0
#     for j in house:
#         if i != j:
#             dist += abs(i-j)
#
#     if answer[1] == dist :
#         answer[0] = min(answer[0], i)
#     elif min(answer[1], dist) == dist :
#         answer[1] = dist
#         answer[0] = i
#
# print(answer[0])