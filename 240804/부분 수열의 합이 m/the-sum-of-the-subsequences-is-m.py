n, m = map(int, input().split())
arr = list(map(int, input().split()))

dp = [1e9] * (m + 1)
dp[0] = 0

for num in arr:
    for i in range(m, num - 1, -1):
        dp[i] = min(dp[i], dp[i - num] + 1)

if dp[m] != 1e9:
    print(dp[m])
else:
    print(-1)