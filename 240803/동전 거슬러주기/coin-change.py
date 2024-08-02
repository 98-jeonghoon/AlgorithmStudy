n, m = map(int, input().split())
coins = list(map(int, input().split()))

dp = [1e9] * (m + 1)
dp[0] = 0

for i in range(1, m + 1):
    for j in range(n):
        if i >= coins[j]:
            if dp[i - coins[j]] == 1e9:
                continue

            dp[i] = min(dp[i], dp[i - coins[j]] + 1)

answer = dp[m]
if answer == 1e9:
    print(-1)
else:
    print(answer)