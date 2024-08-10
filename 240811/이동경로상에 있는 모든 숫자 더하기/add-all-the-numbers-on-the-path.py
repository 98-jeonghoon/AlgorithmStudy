from collections import deque

n, t = map(int, input().split())
command = deque(list(input()))
graph = [list(map(int, input().split())) for _ in range(n)]

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

direct = 0

x, y = n // 2, n // 2
answer = graph[x][y]
def go_commnad(command):
    global direct, x, y, answer, graph
    if command == "R":
        direct = (direct + 1) % 4
        return

    if command == "L":
        direct = (direct - 1) % 4
        return

    if command == "F":
        nx = x + dx[direct]
        ny = y + dy[direct]
        if 0 <= nx < n and 0 <= ny < n:
            answer += graph[nx][ny]
            x, y = nx, ny
            return
        else:
            return

    pass

while command:
    go_commnad(command.popleft())

print(answer)
# for i in graph:
#     print(i)