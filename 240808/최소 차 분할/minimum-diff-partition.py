n = int(input().strip())
numbers = list(map(int, input().strip().split()))

total_sum = sum(numbers)

dp = [False] * (total_sum + 1)
dp[0] = True

for num in numbers:
    for j in range(total_sum, num - 1, -1):
        if dp[j - num]:
            dp[j] = True

min_difference = total_sum

for i in range(1, total_sum):
    if dp[i]:
        difference = abs(total_sum - 2 * i)
        if difference < min_difference:
            min_difference = difference

print(min_difference)