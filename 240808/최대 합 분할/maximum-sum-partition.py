n = int(input())
numbers = list(map(int, input().split()))

total_sum = sum(numbers)

dp = [[False] * (total_sum + 1) for _ in range(total_sum + 1)]
dp[0][0] = True

for num in numbers:
    for i in range(total_sum, -1, -1):
        for j in range(total_sum, -1, -1):
            if dp[i][j]:
                dp[i + num][j] = True
                dp[i][j + num] = True

max_equal_sum = 0
for i in range(total_sum + 1):
    for j in range(i + 1):
        if dp[i][j] and i == j:
            max_equal_sum = max(max_equal_sum, i)

print(max_equal_sum)