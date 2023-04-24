'''
[이진탐색] 4월 24일 수 찾기
N개의 정수에서 X라는 정수 존재 유무 확인

1. input = sys.stdin.readline 입력 시간 감소 (bs기준 296 > 268ms)
2. nn N개의 정수는 list가 아닌 set으로 받기
2-1. binary_search에서는 set으로 받으면 sort를 사용할 수 없어서 런타임 에러
3. print(*[], sep='\n') (176ms)
'''

import sys
input = sys.stdin.readline

n = int(input())
nn = set(map(int, input().split()))
# nn = list(map(int, input().split()))
m = int(input())
mm = list(map(int, input().split()))

# for i in mm:
#     if i in nn:
#         print(1)
#     else:
#         print(0)

# print(*[1 if dt in nn else 0 for dt in mm], sep = '\n')

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
        print(1)
    else:
        print(0)