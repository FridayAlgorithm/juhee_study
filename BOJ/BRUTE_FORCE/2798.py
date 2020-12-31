#-*- encoding: utf-8 -*-
"""black jack"""
import sys

#n : 카드의 개수
#m : 최댓값
#cards[] : 카드를 담은 리스트


n, m = map(int, sys.stdin.readline().split())
cards= list(map(int, input().split(' ')))
sum = 0

for i in range(0, n-2) : # 0에서부터 j,k를 제외한 뒷자리까지
    for j in range(i+1, n-1) : #i를 제외하고 k전까지
        for k in range(j+1, n) : # i, j를 제외하고 끝까지
            if cards[i] + cards[j] + cards[k] > m : # 세 카들 합한 것이 주어진 최댓값과 비교하여 크다면
                continue #for 문 계속 진행하기
            else : #세 카드를 합한 값이 최댓값보다 작다면
                sum = max(sum, cards[i]+cards[j]+cards[k]) #현재의 sum이 더한 값과 비교했을 때 둘 중 크다면 sum으로 넣는다.

print(sum)


