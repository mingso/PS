def solution(s):
    answer = 0

    ans = ""
    i = 0
    while i < len(s):
        if s[i].isdigit():
            ans += s[i]
            i += 1
        else:
            num = 0
            if s[i] == 'o':
                num = 1
                i += 3
            elif s[i:i + 2] == 'tw':
                num = 2
                i += 3
            elif s[i:i + 2] == 'th':
                num = 3
                i += 5
            elif s[i:i + 2] == 'fo':
                num = 4
                i += 4
            elif s[i:i + 2] == 'fi':
                num = 5
                i += 4
            elif s[i:i + 2] == 'si':
                num = 6
                i += 3
            elif s[i:i + 2] == 'se':
                num = 7
                i += 5
            elif s[i] == 'e':
                num = 8
                i += 5
            elif s[i] == 'n':
                num = 9
                i += 4
            else:
                i += 4

            ans += str(num)

    answer = int(ans)

    return answers