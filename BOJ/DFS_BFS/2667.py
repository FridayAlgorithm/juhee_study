#-*- encoding: utf-8 -*-
"""단지 번호 붙이기"""

# idea : 상,하,좌,우를 표시할 리스트 두 개를 만들어 한 지점의 상/하/좌/우를 모두 탐색하며 단지가 있으 경우 깊이 우선 탐색을 시행한다.
# 참고 : https://itholic.github.io/kata-danji/

import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0 , -1]

n = int(sys.stdin.readline())
apt = [list(sys.stdin.readline()) for _ in range(n)]
cnt = 0
answer = []


def dfs(x, y) :
    global cnt
    apt[x][y] = '0' # 방문했으면 또 방문하지 않기 위해 0 으로 바꾸어줌.
    cnt += 1

    """
    dx[0]&dy[0] : (-1,0) 상
    dx[1]&dy[1] : (0,1) 우
    dx[2]&dy[2] : (1,0) 하
    dx[3]&dy[3] : (0,-1) 좌
    """
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny <0 or ny >= n: # 범위를 벗어나는 탐색 (가장 자리들)
            continue
        if apt[nx][ny] == '1' : # 주변에 1이 있으면 하나의 단지로 파악하고 깊이 우선 탐색
            dfs(nx,ny)


# 정사각형 단지를 모두 반복하며 단지를 찾아 cnt를 증가시킨다.
for i in range(n):
    for j in range(n):
        if apt[i][j] == '1': # 1일 경우를 찾아 그 주변을 깊이 탐색함.
            cnt = 0
            dfs(i, j)
            answer.append(cnt) # 탐색이 종료되면 총 단지 수를 답 리스트에 붙여준다. cnt는 전역변수로 함수 밖에서도 그 형태로 사용 가능.

print(len(answer))
answer.sort()
for i in answer:
    print(i)