n = int(input())
coins = [0] + list(map(int, input().split()))

dp = [[0] * 4 for _ in range(n + 1)]

dp[1][1] = coins[1]

for i in range(2, n + 1):
    for j in range(4):
        if j > 0:
            # 1칸 올라가는 경우
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + coins[i])
        if i >= 2:
            # 2칸 올라가는 경우
            dp[i][j] = max(dp[i][j], dp[i - 2][j] + coins[i])

print(max(dp[n][j] for j in range(4)))