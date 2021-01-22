#-*- encoding: utf-8 -*-
"""DFS 와 BFS"""
#idea : bfs 와 dfs 의 개념을 익힌다.
# bfs : 1) 큐에 시작 노드를 넣고, 시작 노드를 방문한 표시를 해준다.
#       2) 큐가 존재할 때까지 돌 것 -> 인접한 노드이고, 방문하지 않았다면 큐에 노드를 넣고, 노드 방문 표시

# dfs : 1) 최상단 노드 (스택에서 제일 위 = 제일 마지막으로 들어온 것) 확인
#       2) 최상단 노드에 방문하지 않은 인접노드가 있으면 -> 그 노드를 시작으로 하는 + 그 노드가 방문되었다는 visited를 포함한 dfs를 재귀로 호출
from sys import stdin

n, m, v = map(int, stdin.readline().split())
matrix = [ [0]*(n+1) for _ in range(n+1) ]

for _ in range(m) :
    line = list(map(int, stdin.readline().split()))
    matrix[line[0]][line[1]] = 1
    matrix[line[1]][line[0]] = 1

def bfs(start) :
    queue = [start]
    visited = [start]

    while queue :
        n = queue.pop(0)
        for i in range(len(matrix[start])) :
            if matrix[n][i] == 1 and (i not in visited) :
                visited.append(i)
                queue.append(i)

    return visited

def dfs(start, visited) :
    visited += [start]

    for i in range(len(matrix[start])) :
        if matrix[start][i] == 1 and (i not in visited) :
            dfs(i, visited)

    return visited

print(*dfs(v, []))
print(*bfs(v))

