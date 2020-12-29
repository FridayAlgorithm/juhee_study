#-*- encoding: utf-8 -*-
"""숫자의 합"""

size = int(input())

number = list(map(int, str(input())))

sum = 0
for i in number :
    sum += i

print(sum)