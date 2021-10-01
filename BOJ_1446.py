import sys
import heapq
input = sys.stdin.readline

n, d = list(map(int, input().split()))
position = [i for i in range(100001)]
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(d+1):
    if i != 0:
        position[i] = min(position[i], position[i-1]+1)
    for j in graph:
        if j[0] == i:
            position[j[1]] = min(position[j[1]], position[j[0]]+j[2])

print(position[d])
