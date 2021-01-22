#-*- encoding: utf-8 -*-
"""바이러스"""
#idea : dfs 를 이용하여 연결되어 있는 곳을 깊이 우선 탐색하여 찾아낸다.
import sys

number = int(sys.stdin.readline())
pair_number = int(sys.stdin.readline())

matrix = [[0]*(number+1) for _ in range(number+1)]
#print(matrix)

for _ in range(pair_number) :
    pairs = list(map(int, sys.stdin.readline().split()))
    matrix[pairs[0]][pairs[1]] = 1
    matrix[pairs[1]][pairs[0]] = 1

def dfs(start, visited) :
    visited += [start]

    for i in range(len(matrix[start])) :
        if matrix[start][i] == 1 and (i not in visited) :
            dfs(i, visited)

    return visited

print(len(dfs(1,[]))-1)
