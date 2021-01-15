#-*- encoding: utf-8 -*-
"""색종이 만들기"""

import sys
N = int(sys.stdin.readline())
matrix = []
white, blue = 0, 0

def quad_tree(x, y, n): # 분할정복을 위한 재귀함수
                        # 4등분의 기준이 될 index(x, y)와 그 크기를 넘김
    global blue, white
    color = matrix[x][y] # 현재 color

    for i in range(x, x+n): # n크기 만큼(사분면 크기만큼) 돌다가
        for j in range(y, y+n):
            if matrix[i][j] != color: # 현재 컬러와 다른 컬러를 만나면 
                quad_tree(x, y, n//2) 
                        # 왼쪽 위의 기준점 (x, y)와 n/2 LEFT TOP
                quad_tree(x, y+n//2, n//2) 
                        # 오른쪽 위의 기준점 (x, y+n/2)와 분할한 n/2 RIGHT TOP
                quad_tree(x+n//2, y, n//2) 
                        # 왼쪽 아래의 기준점 (x+n/2, y)와 분할한 n/2 LEFT BOTTOM
                quad_tree(x+n//2, y+n//2, n//2) 
                        # 오른쪽 아래의 기준점 (x+n/2, y+n/2) 와 분할한 n/2 RIGHT BOTTOM
                return
    
    if color == 0:
        white += 1
    else:
        blue += 1


for _ in range(N):
    #matrix.append(list(map(int,sys.stdin.readline().split())))
    matrix.append(list(map(int, ''.join(sys.stdin.readline().split()))))
    
print(matrix)
quad_tree(0, 0, N) # (0, 0) 부터 돌기 시작

print(white)
print(blue)