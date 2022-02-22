import sys

sudoku = []
available = [[[j for j in range(1, 10)] for _ in range(9)] for _ in range(9)]

for _ in range(9):
    sudoku.append(list(map(int, sys.stdin.readline().split())))

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            for k in range(9):
                try:
                    available[i][j].remove(sudoku[i][k])
                except:
                    continue
            for k in range(9):
                try:
                    available[i][j].remove(sudoku[k][j])
                except:
                    continue

            x = (i // 3) * 3
            y = (j // 3) * 3
            for k in range(3):
                for l in range(3):
                    try:
                        available[i][j].remove(sudoku[x+k][y+l])
                    except:
                        continue
        else:
            available[i][j] = [sudoku[i][j]]

print(available)