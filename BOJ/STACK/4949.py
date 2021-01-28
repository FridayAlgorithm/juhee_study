#-*- encoding: utf-8 -*-
"""균형잡힌 세상"""

import sys

while 1 :
    stack = []
    strings = sys.stdin.readline().rstrip()
    flag = 1

    for i in strings :
        if i == '(' or i == '[' :
            stack.append(i)
        elif i == ')' :
            if stack and stack[-1] == '(' :
                stack.pop()
            else :
                flag = 0
                break
        elif i == ']' :
            if stack and stack[-1] == '[' :
                stack.pop()
            else :
                flag = 0
                break

    if strings == '.' :
        break

    if flag and not stack :
        print('yes')
    else :
        print('no')