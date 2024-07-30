# dp[i][j]=max(dp[i−1][j]+a[i][j],dp[i−1][j−1]+a[i][j])

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = graph[0][0]

for i in range(1, n):
    dp[i][0] = dp[i - 1][0] + graph[i][0]

for i in range(1, n):
    dp[0][i] = dp[0][i - 1] + graph[0][i]

for x in range(1, n):
    for y in range(1, n):
        dp[x][y] = max(dp[x - 1][y] + graph[x][y], dp[x][y - 1] + graph[x][y])

answer = -1
for y in range(n):
    answer = max(answer, dp[n - 1][y])

print(answer)