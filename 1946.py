'''
[정렬] 4월 24일 신입사원
서류심사와 면접시험 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자 선발
'''
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    em = [list(map(int, input().split())) for _ in range(n)]
    em.sort()
    # rem = []
    # for i in range(n):
    #     for j in range(i+1, n):
    #         if em[i][0] < em[j][0] and em[i][1] < em[j][0]:
    #             rem.append(em[j])
        
    # nem = [elem for elem in em if elem not in rem]
    # print(len(nem))
    
    cnt = 1
    temp = em[0][1]
    for i in range(1, n):
        if temp > em[i][1]:
            cnt += 1
            temp = em[i][1]
            
    print(cnt)