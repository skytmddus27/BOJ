'''
[그리디] 4/3 체육복

학생들의 번호는 체격 순으로 매겨져 있어,
바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다.

- for loop를 돌 때 원본 리스트를 건드리지 않도록
    - lost_ = lost[:]
- 여벌 체육복을 가져왔더라도 도난당했다면 체육복을 빌려줄 수 없습니다!
    - lost_dd = [x for x in lost if x not in reserve]
    - reserve_dd는 for문과 상관없이 계속 지워져야 함
'''

def solution(n, lost, reserve):
    lost_dd = [x for x in lost if x not in reserve]
    reserve_dd = [x for x in reserve if x not in lost]
    
    lost_dd.sort()
    lost_ = lost_dd.copy()

    for i in lost_dd:
        if i-1 in reserve_dd:
            lost_.remove(i)
            reserve_dd.remove(i-1)
            continue
        elif i+1 in reserve_dd:
            lost_.remove(i)
            reserve_dd.remove(i+1)
    answer = n - len(lost_)
    return answer