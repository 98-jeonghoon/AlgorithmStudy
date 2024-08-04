n = int(input())
numbers = [1, 2, 5]

dp = [0] * (n + 1)
dp[0] = 1

for i in range(n + 1):
    for num in numbers:
        # 만약 만들기 가능한 숫자라면,
        if i >= num:
            dp[i] = (dp[i] + dp[i - num]) % 10007

print(dp[n])