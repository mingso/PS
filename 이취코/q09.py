def solution(s):
    answer = len(s)

    for step in range(1, len(s)// 2 + 1):
        compressed = ""
        pre_word = s[0:step]
        count = 1

        for j in range(step, len(s), step):
            if pre_word == s[j:j+step] :
                count += 1
            else :
                compressed += (str(count) + pre_word) if count >= 2 else pre_word
                pre_word = s[j: j+step]
                count = 1

        compressed += str(count) + pre_word if count >= 2 else pre_word

        answer = min(answer, len(compressed))

    print(answer)
    return answer

solution("ababcdcdababcdcd")