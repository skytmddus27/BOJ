'''
[이진탐색] 4월 28일 공유기 설치
C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하자.
'''

n, c = map(int, input().split())
l = [int(input()) for _ in range(n)]
l.sort()
left, right = 1, l[-1] - l[0]

while left <= right:
    mid = (left + right) // 2
    value = l[0]
    cnt = 1
    for i in range(1, n):
        if l[i] - value >= mid:
            cnt += 1
            value = l[i]
            
    if cnt >= c:
        left = mid + 1
    else:
        right = mid - 1
        
print(right)