#-*- encoding: utf-8 -*-
"""설탕 배달"""
#idea : 5X + 3Y = N 이 만족하도록 가장 작은 수부터 시작하여 식을 만족하는 x, y를 만나면 멈추고 return 함.

n = int(input())

def solve(n) :

    for y in range((n//3)+1) :
        for x in range((n//5)+1) :
            if (5*x+3*y) == n :
                return x + y

    return -1


answer = solve(n)
print(answer)