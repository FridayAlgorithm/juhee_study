#-*- encoding: utf-8 -*-
"""분해합"""
import sys

N = int(sys.stdin.readline())
result = 0

for i in range(1, N+1):
    num = list(map(int, str(i)))
    result = i + sum(num)

    if result == N: 
        print(i)

    if i == N: # 생성자 없는 경우
        print(0)
