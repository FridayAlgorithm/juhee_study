#-*- encoding: utf-8 -*-
"""소수"""
import sys
import math

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

def prime(num) :
    if num < 2:
        return False

    else:
        for i in range(2, num):
            if num%i == 0 :
                return False

        return True

lists = []

for i in range(M, N+1):
    if prime(i) is True:
        lists.append(i)


if lists:
    print(sum(lists))
    print(min(lists))
else :
    print(-1)