#-*- encoding: utf-8 -*-
""" 숫자 카드 2 """
# idea : 이분 탐색을 이용하여 카드가 가지고 있는 숫자를 찾는다.
# 이 때, 카드와 숫자의 매칭을 위해 딕셔너리 자료구조를 활용함.
import sys

def binary_search(value, arr, start, end) :
    if start > end: # start 가 end 보다 커지는 순간 멈추기
        return 0
    
    mid = (start + end) // 2

    if value == arr[mid]:
        return arr[start:end+1].count(value)
    
    elif n < arr[mid]: # 찾고자 하는 value 보다 작으면
        return binary_search(value, arr, start, mid - 1) # mid 기준 왼쪽 돌기

    else:
        return binary_search(value, arr, mid + 1, end) # mid 기준 오른쪽 돌기


number_dict = {}
N = int(sys.stdin.readline()) # 카드 갯수
card_list = list(map(int, sys.stdin.readline().split(' '))) # 카드들

M = int(sys.stdin.readline()) # 찾을 숫자 갯수
number_list = list(map(int, sys.stdin.readline().split(' '))) # 찾을 숫자들

card_list.sort()

for n in card_list:
    start = 0
    end = len(card_list) - 1

    if n not in number_dict:
        number_dict[n] = binary_search(n, card_list, start, end)

answer = []

for i in number_list:
    if i in number_dict:
        answer.append(number_dict[i])
    else:
        answer.append(0)

for i in answer:
    print(i, end=' ')
