def solution(words, queries):
    answer = []

    words.sort()

    words_reverse = []
    for word in words:
        words_reverse.append(word[::-1])
    words_reverse.sort()

    for query in queries:
        wild_cnt = query.count('?')
        wild_start = 1  # 1이면 처음에 ?, 아니면 끝에 ?

        if query[0] != '?':
            wild_start = 0

        count = 0
        if wild_start == 0:
            for word in words:
                if len(word) == len(query) :
                    if word[:len(word)-wild_cnt] == query[:len(word)-wild_cnt]:
                        count += 1
                    else:
                        if count != 0:
                            break
                        elif word[0] > query[0]:
                            break

        else :
            tmp = query[wild_cnt:]
            tmp = tmp[::-1]
            for drow in words_reverse:
                if len(drow) == len(query):
                    if drow[:len(drow) - wild_cnt] == tmp:
                        count += 1
                    else :
                        if count != 0:
                            break
                        elif drow[0] > tmp[0]:
                            break

        answer.append(count)

    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao",] , ["fro??", "????o", "fr???", "fro???", "pro?"]))