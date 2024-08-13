from collections import deque

n, k, u, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

select = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = -1

def bfs():
    global answer
    visited = [[False] * n for _ in range(n)]
    # print("------------------------------")
    # print(select)
    queue = deque(select[:])
    # 전처리
    for _ in range(len(queue)):
        x, y = queue.popleft()
        visited[x][y] = True
        queue.append((x, y, graph[x][y]))

    while queue:
        x, y, now = queue.popleft()
        for direct in range(4):
            nx = x + dx[direct]
            ny = y + dy[direct]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == False and u <= abs(now - graph[nx][ny]) <= d:
                    visited[nx][ny] = True
                    queue.append((nx, ny, graph[nx][ny]))

    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == True:
                cnt += 1

    answer = max(answer, cnt)
    # for i in visited:
    #     print(i)
    # print(cnt)
    # print("-----------------------------------")

def dfs(start_x, start_y):
    if len(select) == k:
        bfs()
        return

    for x in range(start_x, n):
        if x == start_x:
            start_column = start_y
        else:
            start_column = 0

        for y in range(start_column, n):
            if (x, y) not in select:
                select.append((x, y))
                dfs(x, y + 1)
                select.pop()

dfs(0, 0)


print(answer)