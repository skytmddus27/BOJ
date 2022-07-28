import sys
input = sys.stdin.readline

n, m = map(int, input().split())

lines = [input().strip() for _ in range(n)]
pm_dict = {v:i+1 for i, v in enumerate(lines)}
pm_dict_digit = {i+1:v for i, v in enumerate(lines)}

Q = [input().strip() for _ in range(m)]


for q in Q:
    try:
        q = int(q)
        print(pm_dict_digit[q])    
    except:
        print(pm_dict[q])