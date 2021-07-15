def solution(n, k, cmd):
    answer = ''

    arr = list(range(0, n))
    answer = ['O'] * n
    deleted = []

    for command in cmd:
        if len(command) == 1 :
            if command == 'C':
                deleted.append((k, arr.pop(k)))
                if k == len(arr):
                    k -= 1
            elif command == 'Z':
                i, z = deleted.pop()
                arr.insert(i, z)
                if i <= k :
                    k += 1
        else :
            c, t = command.split()
            if c == 'U':
                k -= int(t)
            elif c == 'D':
                k += int(t)

        # if command[0] == 'U':
        #     c, t = command.split()
        #     k -= int(t)
        # elif command[0] == 'D':
        #     c, t = command.split()
        #     k += int(t)
        # elif command[0] == 'C':
        #     deleted.append((k, arr.pop(k)))
        #     if k == len(arr):
        #         k -= 1
        # elif command[0] == 'Z':
        #     (i, z) = deleted.pop()
        #     arr.insert(i, z)
        #     if i <= k:
        #         k += 1

    for (i, z) in deleted:
        answer[z] = 'X'

    answer = ''.join(answer)
    return answer