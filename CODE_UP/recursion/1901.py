#-*- encoding: utf-8 -*-
"""(재귀 함수) 1부터 n까지 출력하기"""

def recursion(num):
    if num == 0:
        return
    recursion(num-1)
    print(num)

ins = int(input())

if __name__ == "__main__":
	recursion(ins)
