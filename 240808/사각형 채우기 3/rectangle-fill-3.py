def count_ways(n):
    MOD = 1_000_000_007

    if n == 0:
        return 1
    elif n == 1:
        return 2

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 2

    for i in range(2, n + 1):
        dp[i] = (2 * dp[i - 1] + 3 * dp[i - 2]) % MOD

    return dp[n]

n = int(input().strip())
print(count_ways(n))