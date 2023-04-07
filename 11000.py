'''
[그리디] 4월 7일 강의실 배정

최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다.
시간초과로 우선순위 큐 코드 참고
'''

import heapq
n = int(input())
cr = []

for _ in range(n):
    s, t = map(int, input().split())
    cr.append([s, t])
    
cr.sort()

room = []
heapq.heappush(room, cr[0][1])

for i in range(1, n):
    # 현재 회의실 끝나는 시간보다 다음 회의 시작 시간이 빠르면
    if cr[i][0] < room[0]:
        # 새로운 회의실 개설
        heapq.heappush(room, cr[i][1])
    # 현재 회의실에 이어서 회의 개최 가능
    else:
        # 새로운 회의로 시간 변경을 위해 pop 후 새 시간 push
        heapq.heappop(room)
        heapq.heappush(room, cr[i][1])

print(len(room))

# n = int(input())
# cr = []
# for _ in range(n):
#     s, t = map(int, input().split())
#     cr.append([s, t])
    
# cr.sort(key=lambda x: (x[0], x[1]))

# for i in range(n):
#     for j in range(i, n):
#         if cr[i][-1] <= cr[j][0]:
#             cr[i].extend(cr[j])
#             cr[j] = [0, 0]
#             break
  
# cr = [x for x in cr if x != [0,0]]
# print(len(cr))