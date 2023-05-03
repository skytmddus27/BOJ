n = int(input())
nn = list(map(int, input().split()))

dp = [-float('inf')] * n

## 시간 초과
# dp[0] = max(nn)

# for i in range(1, n):
#     for j in range(n-i):
#         dp[i] = max(dp[i], sum(nn[j:j+i+1]))
        
# print(max(dp))

dp[0] = nn[0]

for i in range(1, n):
    dp[i] = max(dp[i-1] + nn[i], nn[i])

print(max(dp))