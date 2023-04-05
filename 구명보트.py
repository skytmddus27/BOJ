from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    dq = deque(people)
    while len(dq) > 1:
        if dq[0] + dq[-1] <= limit:
            dq.popleft()
        answer += 1    
        dq.pop()
    if dq:
        answer+= 1
    return answer

'''
[그리디] 4월 5일 구명보트

무게 제한의 딱 중간인 경우에는 그들끼리 타는게 가장 적절하다 생각하여
제한의 중간보다 작은값, 같은값, 큰값으로 나누어 리스트를 만들었으나...
'''

def solution(people, limit):
    people.sort()
    
    p1 = []
    p5 = []
    p9 = []
    
    for i in people:
        if i < limit/2:
            p1.append(i)
        elif i == limit/2:
            p5.append(i)
        else:
            p9.append(i)
            
    answer = len(p5) // 2
    
    p1c = p1.copy()
    for i in p1:
        for j in p9:
            if i + j > limit:
                answer += 1
                p9.remove(j)
            else:
                answer += 1
                p1c.remove(i)
                p9.remove(j)
                break
    
    if len(p1c) > 0:
        answer += len(p1c)
    elif len(p5) % 2 == 1:
        answer += 1
        
    if len(p9) > 0:
        answer += len(p9)

    return answer
