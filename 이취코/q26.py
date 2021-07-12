n = int(input())
cards = []

for _ in range(n):
    cards.append(int(input()))

cards.sort()

answer = 0
sum = 0
while len(cards) > 1:
    print(len(cards))
    if sum != 0:
        sum += cards[0]
        if 2 < len(cards) and sum + cards[1] < cards[1] + cards[2]:
            cards.insert(1, sum)
        else :
            cards.append(sum)
        answer += sum
        sum = 0

    elif 0 == len(cards)-1:
        sum += cards[0]
        answer += sum

    else :
        sum += cards[0]

    cards.remove(cards[0])


answer += sum
answer += cards[0]

print(answer)