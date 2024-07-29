MOD = 1000000007

def count_ways(n):
    if n == 1:
        return 2
    if n == 2:
        return 7

    dp = [0] * (n + 1)

    dp[1] = 2
    dp[2] = 7
    
    for i in range(3, n + 1):
        dp[i] = (2 * dp[i - 1] + 3 * dp[i - 2]) % MOD
    
    return dp[n]

import sys
input = sys.stdin.read
n = int(input().strip())

print(count_ways(n))