#-*- encoding: utf-8 -*-
"""카드2"""
from collections import deque

number = int(input())
cards = deque()
count = 0

for i in range(1, number + 1) :
    cards.append(i)


while len(cards) != 1 :

   cards.popleft()

   cards.append(cards.popleft())


print(cards.popleft())

"""시간 초과 난 것
#-*- encoding: utf-8 -*-


number = int(input())
cards = []
count = 0

for i in range(1, number + 1) :
    cards.append(i)

while len(cards) != 0 :
    count += 1
    if count%2 == 1 :
       cards.pop(0)

    else :
       cards.append(cards.pop(0))

    if len(cards) == 1 :
        print(cards.pop(0))
        break


"""
