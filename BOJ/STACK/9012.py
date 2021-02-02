#-*- encoding: utf-8 -*-
"""괄호"""

size = int(input())

stack = []

for _ in range(size) :
    parens = list(input())
    while len(parens) != 0 :
        if parens[0] == ')' or parens[-1] == '(' :
            print('NO')
            break
        else :
            if '(' and ')' in parens :
                parens.remove('(')
                parens.remove(')')
            else :
                print('N0')
                break

    if len(parens) == 0:
        print('YES')


""""
다른 사람 코드

n = int(input())
def check(brackets) :
    stack = []
    for i in brackets :
        if i == "(" :
            stack.append(i)
        else : # ')'를 입력받았으나 이전에 '('를 입력받은 적이 없으면 vps 성립 X
            if not stack :
                print("NO")
                return
            else : #stack에 (가 있으면
                stack.pop() #stack에서 (를 pop시킨다.
    
    if not stack: # 리스트를 전부 돌았는데 stack에 남아있는 게 없다면
        print("YES") # VPS 성립
        return
    else : #리스트를 전부 돌았는데 stack에 남아있는 게 있으면
        print("NO") # VPS 성립하지 않음
        return 
"""

