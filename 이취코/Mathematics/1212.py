import sys

x = sys.stdin.readline().rstrip()
octTObi = {0: "000", 1: "001", 2: "010", 3: "011", 4: "100", 5: "101", 6: "110", 7: "111"}

answer = ""

for i in x:
    bi = octTObi[int(i)]
    answer += bi

print(answer.lstrip("0") if answer != "000" else "0")

# x = sys.stdin.readline().rstrip()
# num = int('0o'+x, 8)
# print(format(num, 'b'))