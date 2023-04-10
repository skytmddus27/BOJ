'''
[DFS/BFS] 4월 10일 DFS와 BFS
시작점부터 DFS와 BFS에 따라 방문된 점을 순서대로 출력
'''

from collections import deque

# DFS 함수 정의
def dfs(graph, v, visited):
    visited[v] = True # 현재 노드를 방문 처리
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# BFS 함수 정의
def bfs(graph, start, visited):
    queue = deque([start]) # 큐 구현을 위해 deque 라이브러리 사용
    visited[start] = True # 현재 노드를 방문 처리
    while queue: # 큐가 빌 때까지 반복
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 입력 받기
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n):
    graph[i+1].sort()

# DFS 수행 결과 출력
visited = [False] * (n+1)
dfs(graph, v, visited)
print()

# BFS 수행 결과 출력
visited = [False] * (n+1)
bfs(graph, v, visited)
print()

