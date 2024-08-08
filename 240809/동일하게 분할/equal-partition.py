n = int(input())
numbers = list(map(int, input().split()))

total_sum = sum(numbers)
dp = [False] * (total_sum + 1)
dp[0] = True

for num in numbers:
    for j in range(total_sum, num - 1, -1):
        if dp[j - num]:
            dp[j] = True

answer = False
for i in range(1, total_sum + 1):
    if total_sum - 2 * i == 0:
        answer = True
        break

if answer:
    print("Yes")
else:
    print("No")