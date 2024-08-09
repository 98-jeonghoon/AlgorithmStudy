n = int(input())
coins = [0] + list(map(int, input().split()))

dp = [[0] * 4 for _ in range(n + 1)]

dp[0][0] = 0

# 한칸을 오를수 있는 횟수
for j in range(1, 4):
    # 계단 층수
    for i in range(1, n + 1):
        dp[i][j] = max(dp[i - 1][j - 1] + coins[i], dp[i - 2][j] + coins[i])

# for i in dp:
#     print(i)


print(max(dp[n][j] for j in range(4)))