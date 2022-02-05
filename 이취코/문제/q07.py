n = input()

left = n[:int(len(n)/2)]
right = n[int(len(n)/2):]

left_sum = 0
right_sum = 0

for i in left:
    left_sum += int(i)

for i in right:
    right_sum += int(i)

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")
