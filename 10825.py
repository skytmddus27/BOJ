'''
[정렬] 4월 17일 국영수

1. name을 제외한 나머지는 int형으로 변환해줘야 - 내림차순 정렬 가능
2. list()는 하나의 iterable만 받을 수 있어 대괄호 []로 넣어주기
'''

n = int(input())
s = []
for _ in range(n):
    name, kor, eng, math = input().split()
    s.append([name, int(kor), int(eng), int(math)])
    
ss = sorted(s, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for info in ss:
    print(info[0])