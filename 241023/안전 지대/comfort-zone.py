from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, k):
    queue = deque()
    visited[x][y] = True
    queue.append((x, y))
    area = [graph[x][y]]

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] > k and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    area.append(graph[nx][ny])
    return area

answer_k = 0
answer = 0
for k in range(1, 101):
    visited = [[False] * m for _ in range(n)]
    total_area = []
    for x in range(n):
        for y in range(m):
            if graph[x][y] > k and visited[x][y] == False:
                total_area.append(bfs(x, y, k))
    if len(total_area) > answer_k:
        answer_k = len(total_area)
        answer = k

if (answer, answer_k) == (0, 0):
    print(1, 0)
else:
    print(answer, answer_k)