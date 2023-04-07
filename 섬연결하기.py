'''
[그리디] 4월 7일 섬 연결하기

[섬A, 섬B, cost]
최소 비용으로 모든 섬이 서로 통행 가능하도록
new에 다 때려넣어서 각 섬마다 최소값 하나씩 추출하고 그 중 최대값 하나를 지우려고 했으나
[2, 3, 8] 과 같이 3으로 시작하는 costs가 없을 수 있음.
그렇다고 앞뒤로 다 넣어주면 최소값이 중복될 수 있음.
전혀 모르겠음..
마지막 costs를 기준으로 sort 해보았으나 써먹지 못함.

- kruskal 알고리즘
간선의 가중치를 기준으로 오름차순으로 정렬한 후, 가장 작은 간선부터 시작하여,
사이클을 형성하지 않는 간선을 하나씩 선택하여 최소 신장 트리를 구하는 알고리즘
'''

def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    link = set([costs[0][0]])
    
    while len(link) != n:
        for v in costs:
            if v[0] in link and v[1] in link:
                continue    # 건너뛰고 for 문 마저 진행
            if v[0] in link or v[1] in link:
                link.update([v[0], v[1]])
                answer += v[2]
                break
            
    return answer

# def solution(n, costs):
#     costs.sort(key=lambda x: x[2])
#     inf = float('inf')
#     new = [[[inf] for _ in range(n+1)] for _ in range(n)]
#     for x, y, z in costs:
#         new[x][y] = z
#     all = []
#     for i in range(n):
#         all.append(min(new[i]))
#     all.remove(max(all))
#     answer = sum(all)
#     return answer