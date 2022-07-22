from collections import deque
t = int(input())
for i in range(t):
    p = input()
    n = int(input())
    x = deque(input()[1:-1].split(','))

    rev = 0
    if n == 0:
        x = []
    
    for j in p:
        if j == 'R':
            rev += 1
        elif j == 'D':
            if len(x) == 0:
                print('error')
                break
            else:
                if rev % 2 == 0:
                    x.popleft()
                else:
                    x.pop()

    else:
        if rev % 2 == 0:
            print("["+",".join(x)+"]")
        else:
            x.reverse()
            print("["+",".join(x)+"]")