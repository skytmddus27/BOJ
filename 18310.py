'''
[그리디] 4/3 안테나

효율성을 위해 안테나로부터 모든 집까지의 거리의 총 합이 최소가 되도록 설치

시간 초과... > 질문 게시판 코드 활용
안테나의 위치를 A에서 A+1로 옮기면
현재 총 거리에서 1부터 A에 위치한 집들에서의 거리는 1씩 늘어나고,
A+1부터 100000에 있는 집들에서의 거리는 1씩 줄어들어서 이에 맞춰 총 거리 조절

Q. else: break 그러면 계속 감소하다가 더 이상 감소하지 않으면 반복문을 중지한다는 것
이 뜻이 감소하다가 증가 추세를 걷는 다는 건데, 다시 감소 추세를 보여서 뒤에서 더 낮은 값이 나올 확률은 없나?
'''
from collections import Counter

INF = float('inf')

n = int(input())
houses = list(map(int, input().split()))
counter = Counter(houses)

count = 0
# 처음에는 모든 집들과의 거리를 구함
total_dist = sum(houses)
min_total_dist = INF
result_pos = 1
for pos in range(1, 100001):
    # count와 n-count를 구하고 전체 거리를 계산함
    total_dist += count
    total_dist -= n - count
    # 이전까지의 최소 거리와 비교함
    if min_total_dist > total_dist:
        min_total_dist = total_dist
        result_pos = pos
    else:
        # 더 이상 거리가 감소하지 않으면 반복문을 중지함
        break
    # pos보다 작은 집들의 개수를 더해줌
    count += counter[pos]

print(result_pos)

# import statistics

# n = int(input())
# house = list(map(int, input().split()))

# result = float('inf')
# if statistics.mean(house) <= statistics.median(house):
#     for i in range(min(house), int(statistics.mean(house))+1):
#         sum = 0
#         for j in house:
#             sum += abs(i - j)
#         if sum < result:
#             min_idx = i
#             result = sum
# else:
#     for i in range(int(statistics.mean(house)), max(house)+1):
#         sum = 0
#         for j in house:
#             sum += abs(i - j)
#         if sum < result:
#             min_idx = i
#             result = sum
        
# print(min_idx)