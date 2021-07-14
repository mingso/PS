def solution(n, k, cmd):
    answer = ''

    arr = []
    deleted = []
    for i in range(n):
        arr.append(i)

    for command in cmd:
        c = command[0]
        if c == 'U':
            tmp = command.split()
            k -= int(tmp[1])
        elif c == 'D':
            tmp = command.split()
            k += int(tmp[1])
        elif c == 'C':
            deleted.append( (k, arr[k]) )
            # deleted.append(arr[k])
            arr.remove(arr[k])
            if k == len(arr):
                k -= 1
            else:
                k += 1
        elif c == 'Z':
            z = deleted.pop()
            for i in range(1, z):
                if arr[i - 1] < z < arr[i]:
                    arr.insert(i, z)

        print(arr)


    return answer