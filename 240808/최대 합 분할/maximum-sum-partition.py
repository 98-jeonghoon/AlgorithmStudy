n = int(input())
numbers = list(map(int, input().split()))

total_sum = sum(numbers)

dp = [False] * (total_sum + 1)
dp[0] = True

max_sum_value = 0

for num in numbers:
    new_dp = dp[:]
    for j in range(total_sum - num, -1, -1):
        if dp[j]:
            new_dp[j + num] = True
            if new_dp[j + num] == True and (j + num) * 2 <= total_sum:
                max_sum_value = max(max_sum_value, j + num)
    dp = new_dp

print(max_sum_value)