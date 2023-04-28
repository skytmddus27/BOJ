# 시도 1
## 초기에 왜 1분을 더 기다리고 28분이지 한참을 고민했다
## 20분에 끝내면 되는거 아닌가 싶었는데, 이건 심사를 시작한 시간이고 끝난 시간을 기록해야 하므로 30분으로 더 길다.

# 시도 2
## 그러면 애초에 끝나는 시간으로 맞춰서 정렬하면 되는 거 아닌가 했더니 시간초과
## 맞다 1,000,000,000 이었지 ^^

# def solution(n, times):
#     tl = []
#     for t in times:
#         for i in range(n):
#             tl.append(t*(i+1))
#     tl.sort()
#     print(tl)
#     return tl[n-1]

# 쩝..
def solution(n, times):
    low = 1
    high = max(times) * n
    
    while low <= high:
        mid = (low + high) // 2
        cnt = 0
        for t in times:
            cnt += mid // t
            if cnt >= n: break
            
        if cnt >= n:
            high = mid - 1
        else:
            low = mid + 1
            
    return(low)