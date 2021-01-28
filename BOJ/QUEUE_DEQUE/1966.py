#-*- encoding: utf-8 -*-
"""프린터 큐"""
#idea : 문서의 순서와 우선순위에 대한 리스트를 각각 만들어 준 뒤, 조건에 따라 함께 붙였다 삭제했다를 반복한다.
import sys

#case : 테스트 케이스 개수
#number : 문서의 개수
#document : 몇 번째인지 궁금한 문서의 인덱스
#index : 각 문서의 인덱스

case = int(input())

for i in range(case) :
    number, document = map(int, sys.stdin.readline().split(' '))
    priority = list(map(int, input().split(' ')))
    idx = list(x for x in range(number))
    final_idx = []
    max_priority = max(priority)

    while len(priority) != 0:
        if  priority[0] == max(priority) : # 가장 중요도가 큰 문서를 만나면 출력
            priority.pop(0)
            final_idx.append(idx.pop(0))


        else : # 아니면 뒤에 붙인다.
            priority.append(priority.pop(0))
            idx.append(idx.pop(0))


    print(final_idx.index(document) + 1)
