from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, now):
    queue = deque()
    visited[x][y] = True
    queue.append((x, y))
    block = [(x, y)]

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == now and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    block.append((nx, ny))
    # 터질경우 그냥 바로 리턴
    if len(block) >= 4:
        return True, block
    # 터지지 않을 경우
    else:
        # visited 를 다시 False로 바꿔줌
        for x, y in block:
            visited[x][y] = False
        return False, block

# 터지게 되는 블록수
boom_blocks = []
blocks = []
for x in range(n):
    for y in range(n):
        if visited[x][y] == False:
            flag, block = bfs(x, y, graph[x][y])
            if flag == True:
                boom_blocks.append(block)
            else:
                blocks.append(block)

answer = 0
for block in boom_blocks:
    answer = max(len(block), answer)

for block in blocks:
    answer = max(len(block), answer)

print(len(boom_blocks), answer)