n = int(input().strip())
numbers = list(map(int, input().strip().split()))


total_sum = sum(numbers)
half_sum = total_sum // 2


dp = [False] * (half_sum + 1)
dp[0] = True

for num in numbers:
    for j in range(half_sum, num - 1, -1):
        if dp[j - num]:
            dp[j] = True

for i in range(half_sum, -1, -1):
    if dp[i]:
        closest_sum = i
        break

min_difference = abs(total_sum - 2 * closest_sum)

print(min_difference)