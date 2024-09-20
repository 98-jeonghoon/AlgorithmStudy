from collections import deque

m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(m)]
paint = [list(map(int, input().split())) for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

pos = []

for x in range(m):
    for y in range(n):
        if paint[x][y] == 1:
            pos.append((x, y))

max_value = 0
for x in range(m):
    for y in range(n):
        max_value = max(max_value, graph[x][y])

left = 1
right = max_value

def bfs(x, y, mid):
    visited = [[False] * n for _ in range(m)]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < m and 0 <= ny < n:
                if visited[nx][ny] == False and abs(graph[x][y] - graph[nx][ny]) <= mid:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

    for x, y in pos:
        if visited[x][y] == False:
            return False
    return True


answer = 1e9

while left <= right:
    mid = (left + right) // 2

    if(bfs(x, y, mid)):
        right = mid - 1
        answer = min(answer, mid)
    else:
        left = mid + 1

print(answer)