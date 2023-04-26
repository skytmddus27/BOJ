# 81% 런타임 에러 -> high = sum(l) // n 초기 설정한 값보다 클 수 있어 +1 해줌

import sys
input = sys.stdin.readline

# 오영식이 이미 가지고 있는 랜턴의 개수 k, 필요한 랜선의 개수 n
k, n = map(int, input().split())
# k개의 랜선 길이
l = [int(input()) for _ in range(k)]

low = 1
high = sum(l) // n + 1

while low <= high:
    mid = (low + high) // 2
    cnt = 0
    for i in l:
        cnt += i // mid
        
    if cnt < n:
        high = mid - 1
    else:
        low = mid + 1

print(high)