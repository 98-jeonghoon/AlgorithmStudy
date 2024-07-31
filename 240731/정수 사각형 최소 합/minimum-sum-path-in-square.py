n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][n - 1] = graph[0][n - 1]

for y in range(n - 2, -1, -1):
    dp[0][y] = dp[0][y + 1] + graph[0][y]

for x in range(1, n):
    dp[x][n - 1] = dp[x - 1][n - 1] + graph[x][n - 1]

for y in range(n - 2, -1, -1):
    for x in range(1, n):
        dp[x][y] = min(dp[x - 1][y] + graph[x][y], dp[x][y + 1] + graph[x][y])

print(dp[n - 1][0])