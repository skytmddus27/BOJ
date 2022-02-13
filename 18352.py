# 도시의 개수 n, 도로의 개수 m, 거리 정보 k, 출발 도시의 번호 x
n, m, k, x = map(int, input().split())
# 간선 정보 담기
edges = []

# a -> b 도시로 이동하는 단방향 도로
for _ in range(m):
    a, b = map(int, input().split())
    edges.append((a, b))
    
INF = int(1e9)
dist = [INF] * (n + 1)

def bf(start):
    dist[start] = 0
    for i in range(m):
        cur = edges[i][0]
        next_node = edges[i][1]
        if dist[cur] != INF and dist[next_node] > dist[cur] + 1:
            dist[next_node] = dist[cur] + 1
    return dist

if k in bf(x):
    for i in range(n + 1):
        if bf(x)[i] == k:
            print(i)
else:
    print(-1)
