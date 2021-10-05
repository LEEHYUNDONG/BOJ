# 징검다리 달리기 2
import sys
import heapq
import math
input = sys.stdin.readline

n, f = list(map(int, input().split()))
plot = [list(map(int, input().split())) for _ in range(n)]
INF = int(1e9)
distance = [INF]*(f+1)
plot.sort(key=lambda x: x[1])
graph = [[] for _ in range(n)]

# for i in range(len(plot)):
#     for j in range(i+1, len(plot)):
#         dist = math.sqrt((plot[i][0]-plot[j][0])**2 +
#                          (plot[i][1]-plot[j][1])**2)
#         graph[plot[i][1]].append(dist, plot[j][0])

def dijskstra(x, y):
    q = []
    heapq.heappush(q, (0, x, y))
    distance[y] = 0
    while q:
        dist, rx, ry = heapq.heappop(q)
        # if dist > distance[ry]:
        #     continue
        for dx, dy in plot:
            if abs(dx-rx) <= 2 and abs(dy-ry) <= 2:
                cost = math.sqrt((dx-rx)**2 + (dy-ry)**2) + dist
                #if dx != rx or dy != ry:
                if cost < distance[dy]:
                    distance[dy] = cost
                    heapq.heappush(q, (cost, dx, dy))
                    print(dx, dy)
        # if ry == f:
        #     break


if plot[-1][1] < f:
    print(-1)
else:
    dijskstra(0, 0)
    #print(math.ceil(sum(distance[1:])))
    print(distance)
