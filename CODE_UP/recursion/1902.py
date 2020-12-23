#-*- encoding: utf-8 -*-
"""(재귀 함수) 1부터 n까지 역순으로 출력하기"""

def recursion(num):
    if num == 0:
        return
    print(num)
    recursion(num-1)

ins = int(input())

if __name__ == "__main__":
	recursion(ins)
