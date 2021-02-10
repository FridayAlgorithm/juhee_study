#-*- encoding: utf-8 -*-
"""요세푸스 문제 0"""
#idea : 오리지널 리스트와 인덱스마다 증가하여 숫자를 뽑아내는 리스트를 만들어 숫자를 돌면서 계속 리스트에 갱신해줌.

import sys
from collections import deque

numbers,index = map(int, sys.stdin.readline().split(' '))
member = deque()
count = 0
answer = []

for i in range(numbers) :
    member.append(i+1)

while len(member) != 0 :
    member.rotate(-(index-1))
    answer.append(member.popleft())

strList = [str(x) for x in answer]

print("<%s>" %(", ".join(strList)))
