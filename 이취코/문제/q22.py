from collections import deque

def solution(board):
    answer = 0

    now = deque()
    # 0은 가로 1은 세로
    direction = 0
    now.append((0, 0))
    now.append((0, 1))
    n = len(board)

    while now.count((n-1, n-1)) == 0 :
        x = now[1][0]
        y = now[1][1]
        if direction == 0:
            if board[x][y + 1] == 0:
                now.popleft()
                now.append((x, y + 1))

            elif x + 1 < n and y > 0 and board[x + 1][y - 1] == 0 and board[x + 1][y] == 0:
                now.popleft()
                now.append((x + 1, y))
                direction = 1

            elif x + 1 < n and board[x + 1][y - 1] == 0 and board[x+1][y] == 0:
                now.popleft()
                now.popleft()
                now.append((x + 1, y - 1))
                now.append((x + 1, y))

        else :
            if x + 1 < n and board[x+1][y] == 0:
                   now.popleft()
                   now.append((x+1, y))

            elif y + 1 < n and board[x - 1][y +1] == 0 and board[x][y+1] == 0:
                now.popleft()
                now.append((x, y+1))
                direction = 0

            elif y + 1 < n and board[x - 1][y + 1] == 0 and board[x + 1][y] == 0:
                now.popleft()
                now.append((x + 1, y - 1))
                now.append((x + 1, y))

        answer += 1

    return answer

print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
