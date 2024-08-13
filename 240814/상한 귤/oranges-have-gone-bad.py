from collections import deque

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

tangerine = []
for x in range(n):
    for y in range(n):
        if graph[x][y] == 2:
            tangerine.append((x, y))
            graph[x][y] = 0


def bfs():
    queue = deque(tangerine[:])
    visited = [[False] * n for _ in range(n)]
    new_graph = [[-1] * n for _ in range(n)]
    
    for _ in range(len(queue)):
        x, y = queue.popleft()
        visited[x][y] = True
        new_graph[x][y] = 0
        queue.append((x, y))
        
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == False and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    new_graph[nx][ny] = new_graph[x][y] + 1
                    queue.append((nx, ny))
    return new_graph, visited

new_graph, visited_graph = bfs()

for x in range(n):
    for y in range(n):
        if visited_graph[x][y] == False and new_graph[x][y] == -1 and graph[x][y] == 1:
            new_graph[x][y] = -2

for i in new_graph:
    print(*i)