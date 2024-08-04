n, m = map(int, input().split())
numbers = list(map(int, input().split()))

dp = [-1] * (m + 1)
dp[0] = 0

for number in numbers:
    for i in range(m, number - 1, -1):
        if dp[i - number] != -1:
            dp[i] = max(dp[i], dp[i - number] + 1)

if dp[m] == -1:
    print("No")
else:
    print("Yes")