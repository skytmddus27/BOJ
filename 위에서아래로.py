'''
[정렬] 4월 17일 위에서 아래로

sorted를 쓰면 안되는 문제인가요?
'''

n = int(input())
s = []
for _ in range(n):
    s.append(int(input()))

s = sorted(s, reverse=True)
for i in s:
    print(i, end=' ')