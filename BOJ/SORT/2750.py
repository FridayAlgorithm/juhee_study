#-*- encoding: utf-8 -*-
"""수 정렬하기"""

N = int(input())
answer = []

for _ in range(N):
    answer.append(int(input()))

answer.sort()

for i in answer:
    print(i)