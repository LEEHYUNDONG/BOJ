#k 번째 수
n = int(input())
k = int(input())
data = [i for i in range(1, n**2+1)]
print(data)

# def binary_search(target, start, end):
#     while start <= end:
#         mid = (start + end)//2
#         if mid == target:
#             return mid
#         elif mid > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None
# init data
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(i*j)

#print(binary_search(k-1, 0, n*n))
data = [i for i in range(1, n+1)] 


# def binary_search(i, target, start, end):
#     while start <= end:
#         mid = (start+end) // 2
#         if data[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return mid

# for i in range(1, (n**2)+1):
#     binary_search(i, k, 0, )


#result = binary_search(array, target, 0, n-1)
# if result == None:
#     print('원소가 존재하지 않습니다.')
# else:
#     print(result+1)
