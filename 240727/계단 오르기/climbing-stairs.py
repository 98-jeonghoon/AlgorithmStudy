n = int(input())
dp = [0] * (10001)
dp[0] = 0
dp[1] = 0
dp[2] = 1
dp[3] = 1

if n <= 3:
    print(dp[n])
    exit(0)
for i in range(4, n + 1):
    dp[i] = dp[i - 2] + dp[i - 3]

print(dp[n])