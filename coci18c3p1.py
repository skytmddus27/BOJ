# 문제 : https://dmoj.ca/problem/coci18c3p1
# 시도1 : H 다음에 O 다음에 N 다음에 I가 나온다면 ans에 추가
n = 'HONIHONI'
ans = 0

for i in range(len(n)):
    if n[i] == 'H':
        for j in range(i+1, len(n)):
            if n[j] == 'O':
                for k in range(j+1, len(n)):
                    if n[k] == 'N':
                        for h in range(k+1, len(n)):
                            if n[h] == 'I':
                                ans += 1

print(ans)

## HONI 갯수 세기
'HONI' in 'OHONIHONI'
'OHONIHONI'.index('HONI')
'OHONIHONI'.count('HONI')

## 중복값 제거
n = 'HHHHOOOONNNNIIIIH'
a = ''.join(set(n))
print(a)

b = ''.join(dict.fromkeys(n))
print(b)

from collections import OrderedDict
c = ''.join(OrderedDict.fromkeys(n))
print(c)

# n회차 시도,,
## problem : 'HNOIIONI' 처럼 문자열 H, O, N, I만으로 구성된 리스트에서 'HONI'가 연속된 것이 아닌 떨어져 있는 경우
n = 'HNOIIONI'

## 연속된 중복 값 제거
def list_overlap_del(input_list):
    list_temp = []

    for i in range(len(input_list)):
        if i == 0:
            list_temp.append(input_list[i])
        elif list_temp[-1] != input_list[i]:
            list_temp.append(input_list[i])
    return list_temp
    
dn = list_overlap_del(n)
##  H, O, N, I가 포함되면 append
nn = []
for i in range(len(dn)):
    if dn[i] == 'H' or dn[i] == 'O' or dn[i] == 'N' or dn[i] == 'I':
        nn.append(dn[i])
## list 값 join하고 'HONI'가 있으면 count
''.join(nn).count('HONI')

# github 참고 https://github.com/egsy/zingaro-ltc/blob/d4ca7f9c01289f11a8ddda4c036595ad00740b4f/03/3-2_coci18c3p1.py
HONI = 'HONI'
string = input()
honi_count = 0
char = 0
letter = 0

for char in range(len(string)):
    if string[char] == HONI[letter]:
        letter = letter + 1
        if letter == 4:
            letter = 0
            honi_count = honi_count + 1
print(honi_count)
