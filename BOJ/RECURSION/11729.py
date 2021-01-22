#-*- encoding: utf-8 -*-
"""하노이탑 이동 순서"""
#idea : n개의 판을 옮길 때 먼저 n-1개의 판을 중간에 놓고 제일 큰 것을 3으로 올김. 그리고 다시 n-1개의 판을 2에서 3으로 옮김.
#start=1, mid=2, end=3


def hanoitop(pan, start, mid, end) :
    if pan == 1 :
        print(start, end)
    else :
        hanoitop(pan-1, start, end, mid)
        print(start, end)
        hanoitop(pan-1, mid, start, end)

# n-1개를 start에서 mid 옮기기
# 남은 1개를 start에서 end로 옮기기
# n-1개를 mid에서 end로 옮기기

pan_sum = int(input())
move_sum = 0

for pan in range(pan_sum) :
    move_sum *= 2
    move_sum += 1

print(move_sum)
hanoitop(pan_sum, 1, 2, 3)