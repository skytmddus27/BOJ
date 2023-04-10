'''
[DFS/BFS] 4월 10일 음료수 얼려먹기
생성되는 총 아이스크림의 개수를 구하라.

Q. 재귀적으로 dfs 방문처리를 하면 return True가 모든 0지점에서 발생해서 
0을 모두 count 하는 것은 아닌지...
'''
from collections import deque
n, m = map(int, input().split())
ice = [list(map(int, input())) for _ in range(n)]

def dfs(x, y):     
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if ice[x][y] == 0:
        ice[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        print(ice)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
            
print(result)