#-*- encoding: utf-8 -*-
"""소수 찾기"""

import sys
import math

n = int(sys.stdin.readline())
lists = list(map(int, sys.stdin.readline().split()))
count = 0


def prime(num) :
    if num < 2:
        return False

    else:
        for i in range(2, int(math.sqrt(num))):
            if num%i == 0 :
                return False

        return True


for i in lists :
    if prime(i) is True:
        count += 1

print(count)