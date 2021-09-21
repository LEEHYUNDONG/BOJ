# 회의실 배정
n = int(input())
room = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
room.sort(key=lambda x:x[0])
room.sort(key=lambda x:x[1])
end = 0

for x, y in room:
    if end <= x:
        cnt += 1
        end = y
print(cnt)