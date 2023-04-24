'''
[이진탐색] 4월 24일 부품찾기
손님이 요청한 부품이 있으면 yes, 없으면 no 출력
'''

n = int(input())
nn = list(map(int, input().split()))
m = int(input())
mm = list(map(int, input().split()))

# for i in mm:
#     if i in nn:
#         print("yes", end=" ")
#     else:
#         print("no", end=" ")
        
nn.sort()
def binary_search(target, start, end, arr):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False

for i in mm:
    if binary_search(i, 0, n-1, nn):
        print("yes", end=" ")
    else:
        print("no", end=" ")