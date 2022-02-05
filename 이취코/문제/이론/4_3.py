coor = input()

x = int(ord(coor[:1]) - ord('a'))
y = int(coor[1:])-1

count = 0
# x-2 * y-1  // x-2 * y+1 // x+2 * y-1 // x+2 * y+1 //
# x-1  * y-2 // x+1 * y-2 // x-1 * y+2 // x+1 * y+2

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1),
         (-1, -2), (1, -2), (-1, 2), (1, 2)]

if(x >= 2):
    if(y>1): count += 1
    if(y < 7): count += 1

if (x < 6):
    if(y>1): count += 1
    if(y < 7): count += 1

if (y >= 2):
    if (x > 1): count += 1
    if (x < 7): count += 1

if (y < 6):
    if (x > 1): count += 1
    if (x < 7): count += 1

print(count)