'''
[이진탐색] 4월 24일 떡볶이 떡 만들기
손님이 요청한 길이를 얻기 위한 절단기 높이의 최댓값
'''

n, m = map(int, input().split())
rc = list(map(int, input().split()))
# rc.sort(reverse=True)
# s = m // n
# for i in range(rc[0]-s, 0, -1):
#     t = 0
#     for j in rc:
#         if j > i:
#             t += j - i
#     print(t)
#     if t >= m:
#         print(i)
#         break
    
rc.sort()

left, right = 0, rc[-1]
while left <= right:
    mid = (left + right) // 2
    
    t = sum(max(0, j - mid) for j in rc)
    
    if t >= m:
        left = mid + 1
    else:
        right = mid - 1
        
print(right)