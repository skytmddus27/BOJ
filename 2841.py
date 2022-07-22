n, p = map(int, input().split())
ch = [[] for _ in range(7)]
cnt = 0
for i in range(n):
    line, fret = map(int, input().split())
    if ch[line] != [] and ch[line][-1] > fret:
        ch[line].clear()
        cnt += 1
    elif ch[line] != [] and ch[line][-1] == fret:
        ch[line].pop()
    ch[line].append(fret)
    cnt += 1
print(cnt)