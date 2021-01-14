#-*- encoding: utf-8 -*-
"""수 찾기 """
# idea : M을 돌면서 M의 수들이 A에 존재하는지 아닌지 판단하기. M은 반복문을 통해 접근, A에서는 binary search 하면서 M 원소 찾기

import sys

def binary_search(arr, value, start, end) :
    if start > end: # start 가 end 보다 커지는 순간 멈추기
        return False
    
    mid = (start + end) // 2

    if arr[mid] > value: # 찾고자 하는 value 보다 작으면
        return binary_search(arr, value, start, mid - 1) # mid 기준 왼쪽 돌기

    elif arr[mid] < value:
        return binary_search(arr, value, mid + 1, end) # mid 기준 오른쪽 돌기

    else : # 찾으면 반환
        return True


N = int(sys.stdin.readline()) # 
A = list(map(int, (sys.stdin.readline().split(' ')))) # M 안의 원소들이 A 안에 있는지 없는지
M = int(sys.stdin.readline()) # 개수
mArray = list(map(int, (sys.stdin.readline().split(' ')))) # A랑 비교할 값들
A.sort()

for m in mArray:
    if binary_search(A, m, 0, N-1):
        print(1)
    else:
        print(0)


