def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0 : # 기둥
            if y==0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        elif stuff == 1: #보
            if [x, y -1, 0] in answer or [x+1, y-1, 0] in answer or [x-1, y, 1] in answer and [x+1, y, 1] in answer:
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []

    for i in build_frame:
        x, y, stuff, operate = i
        if operate == 0: # 삭제하는 경우
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
        if operate == 1:
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])

    return sorted(answer)


build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1],
               [5, 0, 0, 1,], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]

solution(5, build_frame)