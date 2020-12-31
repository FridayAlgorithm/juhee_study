#-*- encoding: utf-8 -*-
"""손익분기점"""

#idea : 생산 가격이 판매 비용보다 크면 손익분기점이 넘은 것이므로 반복문을 멈춘다.
#첫번째 시도 : 시간초과 (입력값이 21억 이하의 값임..) -> 단순 반복문 이용 불기
#두번째 시도 : 등호방정식을 이용하여 x 값이 커진 구간에서 멈춘다. -> 실패
#세번째 시도 : count 를 돌리는 건 결국 1과 같아지는 것이므로 부등호의 x값을 출력해야 함.


import sys

fix, var, price = map(int, sys.stdin.readline().split(' '))



if var >= price : # 가변 가격이 판매 가격보다 크면 돌릴 필요가 없음.
    print(-1)

else :
    print((fix // (price - var)+1))




