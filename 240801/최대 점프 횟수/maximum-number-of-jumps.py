n = int(input())
arr = list(map(int, input().split()))

dp = [-1e9] * (n + 1)
dp[0] = 0

for i in range(1, n):
    for j in range(i):
        if dp[j] == -1e9:
            continue

        if j + arr[j] >= i:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))