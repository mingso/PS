def solution(food_times, k):
    answer = 0

    i = 0
    while k > 0:
        if food_times[i % len(food_times)] > 0:
            food_times[i % len(food_times)] -= 1
            k -= 1

        i += 1


    answer = i % len(food_times)
    return answer

food = [3, 2, 2]
print(solution(food, 5) + 1)

