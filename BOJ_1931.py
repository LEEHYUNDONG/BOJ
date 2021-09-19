# 회의실 배정
n = int(input())
room = [list(map(int, input().split())) for _ in range(n)]
cnt = 1
room.sort(key=lambda x:x[1]-x[0])
print(room)
room.sort(key=lambda x:x[1])
print(room)
end = room[0][1]

for i in range(1, n):
    if room[i][0] >= end:
        end = room[i][1]
        cnt += 1
    else:
        continue

print(cnt)