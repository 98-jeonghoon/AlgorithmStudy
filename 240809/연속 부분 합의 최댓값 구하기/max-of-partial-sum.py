n = int(input())
numbers = [0] + list(map(int, input().split()))

dp = [-1e9] * (n + 1)

# 첫번째 값은 첫번째 수가 되어야함
dp[0] = 0

for i in range(1, n + 1):
    # 전에 값에서 지금 값을 더한 값이거나, 아니면 지금 값이거나
    dp[i] = max(dp[i - 1] + numbers[i], numbers[i])

print(max(dp[1:]))