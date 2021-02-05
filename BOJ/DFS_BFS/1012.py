#-*- encoding: utf-8 -*-
"""유기농 배추"""

# idea : 단지 번호 붙이기와 비슷한 형식으로 접근한다. 입력받는 x, y 좌표에 주의하자.

import sys
sys.setrecursionlimit(10 ** 9) # 런타임 에러 해결


def dfs(x, y):
    global cnt
    cnt = 0
    
    matrix[x][y] = 0
    cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue

        if matrix[nx][ny] == 1:
            dfs(nx, ny)


T = int(sys.stdin.readline())

for _ in range(T) :
    M, N, K = map(int, sys.stdin.readline().split())
    matrix = [ [0] * N for _ in range(M)]
    answer = []

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for _ in range(K) :
        a, b = map(int, sys.stdin.readline().split())
        matrix[a][b] = 1

    for i in range(M) :
        for j in range(N) :
            if matrix[i][j] == 1 :
                cnt = 0
                dfs(i, j)
                answer.append(cnt)

    print(len(answer))
