n = int(input())
k = int(input())

start, end = 1, k
ans = 0
while start <= end:
    mid = (start + end) //2
    s = 0
    for i in range(1, n+1):
        s += min(mid//i, n)
    if s >= k:
        end = mid - 1
        ans = mid
    if s < k:
        start = mid + 1

print(ans)