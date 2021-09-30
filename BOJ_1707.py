from collections import deque
import sys

k = int(input())
input = sys.stdin.readline


def bfs(start):
    q = deque([start])
    visited[start] = 1
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = -visited[cur]
            else:
                if visited[i] == visited[cur]:
                    return False
    return True


res = []
for i in range(k):
    cnt = 0
    v, e = list(map(int, input().split()))
    graph = [[] for _ in range(v+1)]
    visited = [0]*(v+1)

    for j in range(e):
        a, b = list(map(int, input().split()))
        graph[a].append(b)
        graph[b].append(a)
    flag = True
    for i in range(1, v+1):
        if visited[i] == 0:
            if not bfs(i):
                flag = False
    if flag == False:
        res.append('NO')
    else:
        res.append('YES')

for i in res:
    print(i)
