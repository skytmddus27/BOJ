'''
[정렬] 4월 24일 두 용액
산성 용액과 알칼리성 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만드시오

시도 1: 더한 값을 리스트에 append -> 메모리 초과
시도 2: 더한 값이 c보다 작을 경우 i0, j0 저장 -> 시간 초과 O(n^2)
시도 3: positive, negative 나눠서 진행 -> 시간 초과 O(n^2)
chatGPT: two pointers 사용해서 cur_sum이 음수일 경우 음수를 줄이고 아니면 양수를 줄인다
'''

n = int(input())
lq = list(map(int, input().split()))

# c = float('inf')
# i0, j0 = 0, 0
# for i in range(n):
#     for j in range(i+1, n):
#         if c > abs(lq[i] + lq[j]):
#             c = abs(lq[i]+ lq[j])
#             i0, j0 = i, j
        
# # minc = min(c, key=lambda x: x[2])

# if lq[i0] <= lq[j0]:
#     print(lq[i0], lq[j0])
# else:
#     print(lq[j0], lq[i0])
    
# p, n = [], []
# for i in lq:
#     if i >= 0:
#         p.append(i)
#     else:
#         n.append(i)
        
# p, n = sorted(p), sorted(n, reverse=True)
# if p == [] or n == []:
#     lq = sorted(lq)
#     print(lq[0], lq[1])
# else:
#     c, p0, n0 = float('inf'), 0, 0
#     for pp in p:
#         for nn in n:
#             if c > pp + nn:
#                 c = pp + nn
#                 p0, n0 = pp, nn
                
#     print(nn, pp)

lq.sort()

# two pointers 알고리즘 사용
i, j = 0, n-1
min_sum = float('inf')
while i < j:
    cur_sum = lq[i] + lq[j]
    if abs(cur_sum) < abs(min_sum):
        min_sum = cur_sum
        min_i, min_j = i, j
    if cur_sum < 0:
        i += 1
    else:
        j -= 1
        
print(lq[min_i], lq[min_j])