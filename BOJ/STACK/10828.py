#-*- encoding: utf-8 -*-
"""스택"""
#idea : 스택에 대한 개념을 익힌다.

import sys
from collections import deque

size = int(input())
count = 0

stack = deque()
answer = []


while count < size :
    command = sys.stdin.readline().split()

    if len(command) == 2 :
        stack.append(command[1])
        count += 1

    else :
        if command[0] == 'top' :
            if not stack : #비어있다면
                answer.append(-1)
            else :
                answer.append(stack[-1])

        elif command[0] == 'size' :
            answer.append(len(stack))

        elif command[0] == 'pop' :
            if not stack :
                answer.append(-1)
            else :
                answer.append(stack.pop())


        elif command[0] == 'empty' :
            if not stack : #비어있다면
                answer.append(1)

            else :
                answer.append(0)

        count += 1


for i in answer :
    print(i, end='\n')