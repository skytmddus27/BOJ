'''
[이진탐색] 4월 26일 기타 레슨
시도: 초기에 n // m 크기로 자른 다음 제일 합계가 큰 인덱스에서 뺴는 형식
'''
n, m = map(int, input().split())
nn = list(map(int, input().split()))

# s = n // m
# ss = []
# for i in range(m+1):
#     ss.append(nn[i*s:(i+1)*s])
# if [] in ss:
#     ss.remove([])

# f = sum(max(ss, key=lambda x: sum(x)))
# g = True
# while g:
#     idx = ss.index(max(ss, key=lambda x: sum(x)))
#     if len(ss[idx]) == 1:
#         break
#     ss[idx-1].append(ss[idx][0])
#     ss[idx].remove(ss[idx][0])
#     if f > sum(max(ss, key=lambda x: sum(x))):
#         f = sum(max(ss, key=lambda x: sum(x)))
#     else:
#         g = False
        
# print(f)

# 블루레이 크기 범위: 가장 긴 강의 시간 ~ 모든 강의 시간의 합
low = max(nn)
high = sum(nn)

# 이진 탐색
while low <= high:
    mid = (low + high) // 2  # 현재 탐색 중인 블루레이 크기
    cnt = 1  # 블루레이 개수
    total_time = 0  # 블루레이에 담긴 강의 시간의 합
    for i in nn:
        # 블루레이에 담을 수 있는 경우
        if total_time + i <= mid:
            total_time += i
        # 블루레이에 담을 수 없는 경우
        else:
            cnt += 1
            total_time = i
    
    # 블루레이 개수가 m보다 작거나 같은 경우: 블루레이 크기를 더 작게 해야 함
    if cnt <= m:
        high = mid - 1
    # 블루레이 개수가 m보다 큰 경우: 블루레이 크기를 더 크게 해야 함
    else:
        low = mid + 1

print(low)