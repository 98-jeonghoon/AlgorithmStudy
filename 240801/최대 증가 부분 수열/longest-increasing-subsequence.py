n = int(input())
arr = list(map(int, input().split()))

dp = [0] * (n + 1)

for i in range(n):
    # 선택된 dp 값은 1이 되어야함
    dp[i] = 1
    # i번째 값까지, 해당 원소에 대해 LIS 길이를 확인함
    for j in range(0, i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))