n = int(input())
coins = [0] + list(map(int, input().split()))

# dp[i][j]는 i층에 도착했을 때, 1칸을 j번 사용하여 얻을 수 있는 최대 동전의 개수
dp = [[-1] * 4 for _ in range(n + 1)]

# 초기 조건 설정
dp[1][1] = coins[1]  # 첫 번째 층에 1칸으로 올라갔을 경우
dp[2][0] = coins[2]  # 두 번째 층에 2칸으로 올라갔을 경우

for i in range(3, n + 1):
    for j in range(4):
        # 1칸 올라가는 경우 (최대 3번까지)
        if dp[i-1][j-1] != -1:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + coins[i])
        
        # 2칸 올라가는 경우
        if dp[i-2][j] != -1:
            dp[i][j] = max(dp[i][j], dp[i-2][j] + coins[i])

# 마지막 층에 도달할 수 있는 경우 중 최대값 찾기
result = max(dp[n][j] for j in range(4) if dp[n][j] != -1)
print(result)