#-*- encoding: utf-8 -*-
"""큐 2"""
#idea : 큐에 대한 개념을 익힌다.

import sys
from collections import deque

size = int(input())
count = 0

queue = deque()
answer = []


while count < size :
    command = sys.stdin.readline().split()

    if len(command) == 2 :
        queue.append(command[1])
        count += 1

    else :
        if command[0] == 'front' :
            if not queue : #비어있다면
                answer.append(-1)
            else :
                answer.append(queue[0])


        elif command[0] == 'back' :
            if not queue :
                answer.append(-1)
            else :
                answer.append(queue[-1])

        elif command[0] == 'size' :
            answer.append(len(queue))

        elif command[0] == 'pop' :
            if not queue :
                answer.append(-1)
            else :
                answer.append(queue.popleft())


        elif command[0] == 'empty' :
            if not queue : #비어있다면
                answer.append(1)

            else :
                answer.append(0)


        count += 1


for i in answer :
    print(i, end='\n')