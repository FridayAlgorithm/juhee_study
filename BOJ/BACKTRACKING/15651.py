#-*- encoding: utf-8 -*-
""" N과 M (3) """
import sys

# N : N까지 자연수 중 M개 고르기
N, M = map(int, sys.stdin.readline().split())
result = []

def solve(depth, N, M):
    if depth == M:
        print(' '.join(map(str, result)))
        return
    for i in range(N):
        print(i, "단계")
        print(depth, "길이")
        result.append(i+1)
        solve(depth+1, N, M)
        result.pop()

solve(0, N, M)