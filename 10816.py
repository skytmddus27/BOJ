'''
[이진탐색] 4월 26일 숫자 카드 2
주어진 숫자에 대해 상근이가 몇 개의 카드를 가지고 있는가

시도 1: 이진탐색으로 진행 시 start = mid + 1 로 중간에 건너뛰는 부분으로 실패
시도 2: collections 모듈 사용
'''
from collections import Counter

n = int(input())
nn = list(map(int, input().split()))
m = int(input())
mm = list(map(int, input().split()))

nnn = Counter(nn)
for i in mm:
    print(nnn[i], end = ' ')
    
# nn.sort()
# def binary_search(target, start, end, arr):
#     ans = 0
#     while start <= end:
#         mid = (start + end) // 2
#         if arr[mid] == target:
#             ans += 1
#             start = mid + 1
#         elif arr[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return ans

# for i in mm:
#     print(binary_search(i, 0, n-1, nn), end= " ")