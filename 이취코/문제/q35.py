def ugly_num(n):
    i = 2
    num = 1
    while num < n:
        j = i
        while j % 2 == 0:
            j = j // 2
        while j % 3 == 0:
            j = j // 3
        while j % 5 == 0:
            j = j // 5

        if j == 1:
            num += 1

        i += 1

    return i - 1


print(ugly_num(int(input())))
