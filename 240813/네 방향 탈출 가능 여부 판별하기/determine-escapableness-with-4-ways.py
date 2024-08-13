from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

x, y = 0, 0
queue = deque()
queue.append((x, y))
visited[x][y] = True

while queue:
    x, y = queue.popleft()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == False and graph[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))

if visited[n - 1][m - 1]:
    print(1)
else:
    print(0)