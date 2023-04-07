'''
[그리디] 4월 7일 과제

하루 한 과제를 끝낼 수 있다. 점수를 많이 받을 수 있도록 수행하자.
다음날 과제를 미리 하는게 더 이득일 수도 있다;;
그러면 뒤에서부터 생각해보자
6 5     - 6
4 60    - 4
4 40    - 3
4 10
3 30    - 1
2 50    - 2
1 20
그 날에 할 수 있는 과제 중에 가장 높은 점수를 추출하면 됨.
max score일 때만 dw remove 진행해야함... but how?
'''

n = int(input())
dw = []
for _ in range(n):
    d, w = map(int, input().split())
    dw.append([d, w])
    
dw.sort(key=lambda x: (-x[0], -x[1]))

due = dw[0][0]
sum = 0
for i in range(due, 0, -1):  
    try:
        max_dw = max(filter(lambda x: x[0] >= i, dw), key=lambda x: x[1])
        sum += max_dw[1]
        dw.remove(max_dw)
    except:
        pass
    
print(sum)
            

# import heapq
# n = int(input())
# dw = []
# for _ in range(n):
#     d, w = map(int, input().split())
#     dw.append([d, w])
    
# dw.sort(key=lambda x: (x[0], -x[1]))

# due = []
# heapq.heappush(due, dw[0][0])
# score = dw[0][1]

# for i in range(1, n):
#     if dw[i][0] == due[-1]:
#         pass
#     else:
#         heapq.heappush(due, dw[i][0])
#         score += dw[i][1]
        
# print(score)