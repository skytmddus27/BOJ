import sys

def change(T_all, t):#확률계산반환
    return t / T_all * 100

data = sys.stdin.read()#입력끝까지 받고
tree = data.split('\n')#줄바꿈으로 구분

treedict = {}#딕셔너리로 저장
T_all = 0
for t in tree:
    if t != '':
        T_all += 1
        if t in treedict.keys():
            treedict[t] += 1
        else:
            treedict[t] = 1

res = sorted(treedict.items())

for t in res:
        print("%s %.4f"%(t[0], change(T_all, t[1])))