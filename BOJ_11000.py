# 강의실 배정
import heapq

n = int(input())
room = [list(map(int, input().split())) for _ in range(n)]
room.sort(key=lambda x:x[0])

q = []
heapq.heappush(q, room[0][1])

for i in range(1, n):
    if q[0] > room[i][0]:
        heapq.heappush(q, room[i][1])
    else:
        heapq.heappop(q)
        heapq.heappush(q, room[i][1])

print(len(q))