'''
[DFS/BFS] 4월 10일 미로탈출

(1,1) ~ (N,M)
미로를 탈출하기 위해 움직여야 하는 최소 칸의 개수

DFS
시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면,
가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서
다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회방법

BFS
탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후에,
방문 했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식

https://youtu.be/e7_H8SLZlHY

Q. 위로가거나 왼쪽으로 갈 경우 이미 1 이상의 수가 적혀 있을 수 있는데 
그런 경우 if 문이 없는데 그냥 continue로 진행되는 것인가..?
'''
from collections import deque
n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        # print(queue)
        # print(maze)
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    return maze[n-1][m-1]

print(bfs(0, 0))