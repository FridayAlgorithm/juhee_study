#-*- encoding: utf-8 -*-
"""01타일"""

import sys

N = int(sys.stdin.readline())

MAX = 1000001
permutations = [0] * MAX
permutations[1] = 1
permutations[2] = 2

for i in range(3, N+1):
    permutations[i] = (permutations[i-1] + permutations[i-2])%15746

print(permutations[N])
