'''
[DP] 5월 3일 2XN 타일링
1x2, 2x1 타일로 채우는 방법의 수를 10,007로 나눈 나머지 출력

1 > 1 = 1
2 > 2 = 1 + 1
3 > 3 = 1 + 2
4 > 5 = 1 + 3 + 1
5 > 8 = 1 + 4 + (2 + 1)
6 > 13 = 1 + 5 + (3 + 2 + 1) + 1
7 > 21 = 1 + 6 + (4 + 3 + 2 + 1) + (2 + 1 + 1)
8 > 34
9 > 55
'''
n = int(input())
dp = [0] * (n + 1)
dp[:3] = [0, 1, 2]
for i in range(3, n + 1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n] % 10007)