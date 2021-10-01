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


def dijskstra(x, y):
    q = []
    heapq.heappush(q, (INF, x, y))
    distance[y] = INF
    while q:
        dist, rx, ry = heapq.heappop(q)
        if dist > distance[ry]:
            continue
        for dx, dy in plot:
            cost = math.sqrt((dx-rx)**2 + (dy-ry)**2)
            if dx != rx or dy != ry:
                if cost < distance[dy]:
                    distance[dy] = cost
                    heapq.heappush(q, (cost, dx, dy))
                    print(rx, ry)
        if ry == f:
            break


if plot[-1][1] < f:
    print(-1)
else:
    dijskstra(0, 0)
    print(math.ceil(sum(distance[1:])))
