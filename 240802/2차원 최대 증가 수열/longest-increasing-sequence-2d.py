n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1e9] * m for _ in range(n)]
dp[0][0] = 1

for i in range(1, n):
    for j in range(1, m):
        for x in range(i):
            for y in range(j):
                if dp[x][y] == -1e9:
                    continue
                if graph[i][j] > graph[x][y]:
                    dp[i][j] = max(dp[i][j], dp[x][y] + 1)


max_value = 0
for i in range(n):
    for j in range(m):
        max_value = max(max_value, dp[i][j])
print(max_value)