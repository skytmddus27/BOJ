'''
[정렬] 4월 17일 성적이 낮은 순서로 학생 출력하기

dictionary value를 기준으로 정렬하고 key 출력
'''

n = int(input())
s = {}
for _ in range(n):
    name, score = input().split()
    s[name] = score

ss = dict(sorted(s.items(), key=lambda item: item[1]))

for key in ss.keys():
    print(key, end=' ')