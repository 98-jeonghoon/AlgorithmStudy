def count_tilings(n):
    MOD = 1000000007

    dp = [0] * (n + 1)
    
    dp[0] = 1
    dp[1] = 2
    if n >= 2:
        dp[2] = 7
    
    for i in range(3, n + 1):
        dp[i] = (2 * dp[i-1] + dp[i-2] + 3 * dp[i-3]) % MOD
    
    return dp[n]

n = int(input())

result = count_tilings(n)
print(result)