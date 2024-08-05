n, m = map(int, input().split())
knapsack = [(0, 0)]

for _ in range(n):
    w, v = map(int, input().split())
    knapsack.append((w, v))

dp = [[0] * (n + 1) for _ in range(m + 1)]

for weight in range(1, m + 1):
    for knap in range(1, n + 1):
        knap_weight, knap_value = knapsack[knap]

        if knap_weight > weight:
            dp[weight][knap] = dp[weight][knap - 1]
        else:
            dp[weight][knap] = max(dp[weight][knap - 1], dp[weight - knap_weight][knap - 1] + knap_value)

print(dp[m][n])