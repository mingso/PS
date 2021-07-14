def solution(n, k, cmd):
    answer = ''

    arr = [i for i in range(n)]
    deleted = []

    for command in cmd:
        if len(command) == 1:
            if command == 'C':
                deleted.append((k, arr[k]))
                arr.remove(arr[k])
                if k == len(arr):
                    k -= 1
            elif command == 'Z':
                i, z = deleted.pop()
                arr.insert(i, z)
                if i <= k:
                    k += 1
        else:
            c, t = command.split()
            if c == 'U':
                k -= int(t)
            elif c == 'D':
                k += int(t)

        # if c == 'U':
        #     c, t = command.split()
        #     k -= int(t)
        # elif c == 'D':
        #     c, t = command.split()
        #     k += int(t)
        # elif c == 'C':
        #     deleted.append((k, arr[k]))
        #     arr.remove(arr[k])
        #     if k == len(arr):
        #         k -= 1
        # elif c == 'Z':
        #     (i, z) = deleted.pop()
        #     arr.insert(i, z)
        #     if i <= k:
        #         k += 1

    deleted.sort(key=lambda x: (int(x[1])))

    answer = ['O' for i in range(n - len(deleted))]

    for (i, z) in deleted:
        answer.insert(z, 'X')

    answer = ''.join(answer)
    return answer