#-*- encoding: utf-8 -*-
"""파도반 수열"""
#idea : 피보나치랑 비슷..

import sys

T = int(sys.stdin.readline())
answer = []

for _ in range(T):
    N = int(sys.stdin.readline())
    permutation = [1,1,1]

    for i in range(3, N):
        permutation.append(permutation[i-3]+permutation[i-2])

    answer.append(permutation[-1])

for i in answer:
    print(i)