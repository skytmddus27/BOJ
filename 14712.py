import sys
# lambda와 rstrip()의 동작 원리는 무엇인가
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [[0] * (m + 1) for _ in range(n + 1)]

def dfs(x, y):
    ans = 0
    if y > m:
        x, y = x+1, 1
    if x > n:
        return 0

    if graph[x-1][y] == 0 or graph[x][y-1] == 0 or graph[x-1][y-1] == 0:
        graph[x][y] = 1
        ans += (1 + dfs(x, y+1))
        # 이렇게 하면 연쇄 동작 후 다시 돌아와서 0으로 채우는 건가
        graph[x][y] = 0
    ans += dfs(x, y+1)
    return ans

# 왜 마지막에 1을 더하는가
print(dfs(1, 1) + 1)
