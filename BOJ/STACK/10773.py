#-*- encoding: utf-8 -*-
"""제로"""

temp = []

size = int(input())

for i in range(0,size) :
    number = int(input())
    temp.append(number)
    if number == 0 :
        temp.pop(-1)
        temp.pop(-1)

sum = 0

for i in temp :
    sum += i

print(sum)