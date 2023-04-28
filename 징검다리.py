'''
[이진탐색] 4월 28일 징검다리
바위를 n개 제거한 뒤 각 지점 사이의 거리의 최솟값 중에 가장 큰 값을 return
'''

def solution(distance, rocks, n):
    rocks.sort() # 바위 위치 정렬
    rocks.append(distance) # 도착지점 거리 추가
    left, right = 1, distance # 이진 탐색 시작
    
    answer = 0
    while left <= right:
        mid = (left + right) // 2 # 거리의 최솟값 후보
        prev_rock = 0 # 이전 바위 위치
        remove_cnt = 0 # 제거한 바위 수
        
        for rock in rocks:
            if rock - prev_rock < mid: # 해당 거리 이하로 떨어져 있으면 바위 제거
                remove_cnt += 1
            else: # 해당 거리 이상으로 떨어져 있으면 다음 바위로 이동
                prev_rock = rock
                
        if remove_cnt > n: # 제거한 바위 수가 n개보다 많으면 거리의 최솟값을 줄여야 함
            right = mid - 1
        else: # 제거한 바위 수가 n개 이하면 거리의 최솟값을 늘려야 함
            left = mid + 1
            answer = mid # 현재 거리의 최솟값 중 가장 큰 값 저장
            
    return answer