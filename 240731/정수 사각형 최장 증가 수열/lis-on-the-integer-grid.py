n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[1] * n for _ in range(n)]

pos = []

for x in range(n):
    for y in range(n):
        pos.append((graph[x][y], x, y))

pos.sort()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _, x, y in pos:
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > graph[x][y]:
            dp[nx][ny] = max(dp[nx][ny], dp[x][y] + 1)

answer = 0

for x in range(n):
    for y in range(n):
        answer = max(answer, dp[x][y])

print(answer)