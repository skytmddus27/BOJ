n = int(input())
k = list(map(int, input().split()))

dp = [0] * n
dp[:2] = k[:2]
    
for i in range(2, n):
    # 바로 전 걸 털면 현재는 털 수 없음
    # 전전 걸 털면 현재 털 수 있음
    dp[i] = max(dp[i-1], dp[i-2] + k[i])
    
print(dp[n-1])