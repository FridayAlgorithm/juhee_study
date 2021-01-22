import sys
"""dungchi"""
number = int(input())
pair = []
answer = []

for _ in range(number):
    w, h = map(int, sys.stdin.readline().split())
    pair.append((w, h))

for i in range(len(pair)) :
    count = 1
    for j in range(len(pair)) :
        if pair[i][0] < pair[j][0] and pair[i][1] < pair[j][1] :
                count += 1
    answer.append(count)

for i in answer :
    print i,