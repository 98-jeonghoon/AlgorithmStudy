n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


dx = [1, 0]
dy = [0, 1]
visited = [[False] * m for _ in range(n)]

def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return True
    if visited[x][y] or graph[x][y] == 0:
        return False
    visited[x][y] = True
    for d in range(2):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if dfs(nx, ny):
                return True
    return False

# 좌측 상단에서 DFS 시작
if dfs(0, 0):
    print(1)
else:
    print(0)