#-*- encoding: utf-8 -*-
"""최소 힙"""
import sys

def insert(heap, x):
    heap.append(x)
    i = len(heap) - 1

    while i > 1:
        if heap[i//2] > heap[i] : # 부모가 자식보다 작다면 교체
            heap[i], heap[i//2] = heap[i//2], heap[i] # swap
            i = i // 2    
        else:
            break

def remove(heap):
    minValue = heap[1]
    temp = heap.pop()

    parent = 1
    child = 2

    while child <= len(heap) - 1:
        if child < len(heap) - 1 and heap[child] > heap[child+1]:
            child += 1
        
        if heap[child] >= temp:
            break
    
        heap[parent] = heap[child]

        parent = child
        child *= 2

    if len(heap) != 1:
        heap[parent] = temp
    
    return minValue

n = int(sys.stdin.readline())

heap = [0]

for _ in range(n):
    num = int(sys.stdin.readline())

    if num == 0:
        if len(heap) == 1:
            print(0)
        else:
            print(remove(heap))
    else:
        insert(heap, num)  