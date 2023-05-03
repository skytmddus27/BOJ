'''
[DP] 5월 3일 계단 오르기
1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다.
2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
3. 마지막 도착 계단은 반드시 밟아야 한다.

n이 2일 때까지는 sum(k)
n이 3일 때는 도착점은 무조건 밟아야 하면서 연속 세개는 안되므로 가운데 빼고 10 + 15 = 25
n이 4일 때는 30 + 25 또는 25 + 25
n이 5일 때는 25 + 10 또는 55 + 10
n이 6일 때는 쩝.
'''

# n = int(input())
# k = [int(input()) for _ in range(n)]

# dp = [0] * n
# num = [0] * n
    
# for i in range(n):
#     if i < 2:
#         num[i] = sum(k[:i+1])
#     elif i == 3:
#         num[i] = k[0] + k[2]
#     else:
#         num[i] = max(num[i-1]+k[i], num[i-2]+k[i])
    
# print(dp[n-1])

n = int(input())  # 계단의 개수
stairs = [0]  # 각 계단의 점수를 저장할 리스트, 인덱스는 1부터 시작하도록 0을 추가함
for i in range(n):
    stairs.append(int(input()))

dp = [0] * (n+1)  # 각 계단까지 올라가면서 얻을 수 있는 최대 점수를 저장할 리스트, 인덱스는 0부터 시작함
dp[1] = stairs[1]  # 첫 번째 계단의 점수를 최대 점수로 초기화
if n > 1:
    dp[2] = stairs[1] + stairs[2]  # 두 번째 계단까지 올라가는 경우, 첫 번째 계단에서 1칸 올라온 경우와 2칸 올라온 경우 중 더 큰 값을 선택

for i in range(3, n+1):
    dp[i] = max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i])

print(dp[n])