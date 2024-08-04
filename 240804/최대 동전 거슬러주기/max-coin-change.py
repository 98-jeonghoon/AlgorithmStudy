n, m = map(int, input().split())
coins = list(map(int, input().split()))

dp = [-1e9] * (m + 1)
dp[0] = 0

for i in range(1, m + 1):
    for coin in coins:
        # 만들기 가능하다면
        if i - coin >= 0:
            # 못만드는 방법
            if dp[i - coin] == -1e9:
                continue
            dp[i] = max(dp[i], dp[i - coin] + 1)

if dp[-1] == -1e9:
    print(-1)
else:
    print(dp[-1])