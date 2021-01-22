#-*- encoding: utf-8 -*-
"""별 찍기 - 10"""
#처음 접근법 : 예로, (0,0) ~ (2,2) 까지 3x3 배열에서 가운데가 비어야 하므로 1,1즉 (3/3) 값을 찾아 빈칸을 만들어준다. -> 재귀로 못 품..
#참고한 접근법 : 배열 형태는 동일하나, 1 과 1이 아닐 때만 출력해주는 형식으로 접근하자.


def Star(x, y, num, matrix):
    if num == 1:
        matrix[x][y] = '*'
        return

    div = num // 3
    for i in range (3):
        for j in range (3):
            if i == 1 and j == 1:
                pass
            else:
                Star(x + (i * div), y + (j * div), div, matrix)

def solution():
    matrix = [[' '] * 2201 for i in range(2201)]
    N = int(input())

    Star(0, 0, N, matrix)

    for i in range(N):
        string = ''
        for j in range(N):
            string += matrix[i][j]
        print(string)

solution()


# number = int(input())
# size = int(number / 3)
# stars = []
# for _ in range(number) :
#     stars.append('*')
#
# def star(n) :
#     box = []
#     for i in range(3*len(n)) :
#         for j in range(1,3+1) :
#             if (i%3) == 2 and (j%3) == 2 :
#                 print(' ',end='')
#             else:
#                 print('*', end='')
#             if j % 3 == 0 :
#                 print('\n')
