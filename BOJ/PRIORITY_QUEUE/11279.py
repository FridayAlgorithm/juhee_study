#-*- encoding: utf-8 -*-
"""최대 힙"""
import sys

def insert(heap, x):
    heap.append(x)
    i = len(heap) - 1

    while i > 1:
        if heap[i//2] < heap[i] : # 부모가 자식보다 작다면 교체
            heap[i], heap[i//2] = heap[i//2], heap[i] # swap
            i = i // 2    
        else:
            break

def remove(heap):
    maxValue = heap[1]
    temp = heap.pop()

    parent = 1
    child = 2

    while child <= len(heap) - 1:
        if child < len(heap) - 1 and heap[child] < heap[child+1]:
            child += 1
        
        if heap[child] <= temp:
            break
    
        heap[parent] = heap[child]

        parent = child
        child *= 2

    if len(heap) != 1:
        heap[parent] = temp
    
    return maxValue

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


"""Heap Sort
def heapify(arr, n, i):
    parent = i
    left = i * 2 + 1
    right = i * 2 + 2

    if(left < n and arr[parent] < arr[left]):
        parent = left
    
    if(right < n and arr[parent] < arr[right]):
        parent = right
    
    if(i != parent):
        swap(arr, parent, i)
        heapify(arr, n, parent)

def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]

def heapSort(arr):
    n = len(arr)

    for i in range((n//2)-1, 0, -1):
        heapify(arr, n, i)
    
arr = [0, 1, 2, 0, 0, 3, 2, 1, 0, 0, 0, 0, 0]

heapSort(arr)

for i in range(len(arr)):
    print(arr[i])"""
