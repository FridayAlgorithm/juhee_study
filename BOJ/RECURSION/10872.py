#-*- encoding: utf-8 -*-
"""팩토리얼"""

def fact(num) :
    if num == 1 :
        return 1
    elif num == 0:
        return 1
    return num * fact(num-1)

number = int(input())

answer = fact(number)
print(answer)
