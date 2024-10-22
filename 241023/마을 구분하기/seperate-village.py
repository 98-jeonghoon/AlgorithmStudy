from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = []

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == False and graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1
    return cnt

for x in range(n):
    for y in range(n):
        if graph[x][y] == 1 and visited[x][y] == False:
            answer.append(bfs(x, y))

print(len(answer))
answer.sort()
for i in answer:
    print(i)