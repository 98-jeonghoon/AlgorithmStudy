from collections import deque

r, c, k = map(int, input().split())
graph = [[0] * c for _ in range(r + 3)]
exit = [[False] * c for _ in range(r + 3)]

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

golem = []

for _ in range(k):
    col, d = map(int, input().split())
    golem.append((col - 1, d))

def golem_move(golem_c, d, idx):
    golem_x, golem_y, golem_idx = 1, golem_c, idx

    # 더이상 움직이지 못할때까지 해당 과정을 반복한다
    while True:
        first, second, third = False, False, False
        # 아래로 한칸 이동해본다.
        move_x = golem_x + 1
        check = []
        for direct in range(4):
            nx = move_x + dx[direct]
            ny = golem_y + dy[direct]
            check.append((nx, ny))

        # 만약 아래로 내려가지 못하면
        for nx, ny in check:
            if 0 <= nx < r + 3 and 0 <= ny < c and graph[nx][ny] == 0:
                continue
            else:
                # 내려가지 못한다고 체크
                first = True
                # print("hey")
                break

        # 내려갈 수 있다면 골렘의 좌표를 갱신해주고 아래 로직 무시
        if first == False:
            golem_x = move_x
            continue

        # 서쪽방향으로 회전하면서 내려간다.
        # 서쪽방향으로 한칸 이동한 뒤 내려간다
        move_y = golem_y - 1
        check = []
        for direct in range(4):
            nx = golem_x + dx[direct]
            ny = move_y + dy[direct]
            check.append((nx, ny))

        for nx, ny in check:
            if 0 <= nx < r + 3 and 0 <= ny < c and graph[nx][ny] == 0:
                continue
            else:
                second = True
                break
        check = []
        # 만약 서쪽으로 이동이 가능했다면, 아래쪽도 이동가능한지 봐야함
        if second == False:
            move_x = golem_x + 1
            for direct in range(4):
                nx = move_x + dx[direct]
                ny = move_y + dy[direct]
                check.append((nx, ny))

        for nx, ny in check:
            if 0 <= nx < r + 3 and 0 <= ny < c and graph[nx][ny] == 0:
                continue
            else:
                second = True
                break

        # 만약에 서쪽과 아래쪽으로 이동이 가능하다면 아래 로직 무시
        # 골렘 좌표 갱신
        if second == False:
            golem_x = move_x
            golem_y = move_y
            d = (d - 1) % 4
            continue

        # 동쪽 방향으로 회전하면서 내려간다
        move_y = golem_y + 1
        check = []
        for direct in range(4):
            nx = golem_x + dx[direct]
            ny = move_y + dy[direct]
            check.append((nx, ny))

        for nx, ny in check:
            if 0 <= nx < r + 3 and 0 <= ny < c and graph[nx][ny] == 0:
                continue
            else:
                third = True
                break
        if third == False:
            move_x = golem_x + 1
            check = []
            for direct in range(4):
                nx = move_x + dx[direct]
                ny = move_y + dy[direct]
                check.append((nx, ny))

            for nx, ny in check:
                if 0 <= nx < r + 3 and 0 <= ny < c and graph[nx][ny] == 0:
                    continue
                else:
                    third = True
                    break

        # 만약 동쪽과 아래쪽으로 이동이 가능하다면
        if third == False:
            golem_x = move_x
            golem_y = move_y
            d = (d + 1) % 4
            continue

        # 모두 움직이지 못한다면
        if first == True and second == True and third == True:
            return golem_x, golem_y, d, golem_idx



        pass
    pass

def exit_logic(x, y):
    visited = [[False] * c for _ in range(r + 3)]
    visited[x][y] = True
    queue = deque()
    queue.append((x, y, graph[x][y]))
    value = x
    # print("초기값", value)
    while queue:
        x, y, now = queue.popleft()
        for direct in range(4):
            nx = x + dx[direct]
            ny = y + dy[direct]
            if 0 <= nx < r + 3 and 0 <= ny < c and visited[nx][ny] == False:
                # 만약에 출구 좌표면 같은 블록이 아니라도 이동가능함
                if exit[x][y] == True:
                    if graph[nx][ny] != 0:
                        visited[nx][ny] = True
                        queue.append((nx, ny, graph[nx][ny]))
                        value = max(value, nx)
                else:
                    if graph[nx][ny] == now:
                        visited[nx][ny] = True
                        queue.append((nx, ny, graph[nx][ny]))
                        value= max(value, nx)

    # for i in visited:
    #     print(i)
    return value

def check_body():
    for i in range(3):
        for j in range(c):
            # 만약 하나라도 존재하면
            if graph[i][j] != 0:
                return False
    return True

answer = 0
for i in range(k):
    x, y, d, idx = golem_move(golem[i][0], golem[i][1], i + 1)
    graph[x][y] = idx
    for direct in range(4):
        nx = x + dx[direct]
        ny = y + dy[direct]
        graph[nx][ny] = idx
    # for pp in graph:
    #     print(pp)
    # print()
    exit_x, exit_y = x + dx[d], y + dy[d]
    exit[exit_x][exit_y] = True
    if check_body() == False:
        graph = [[0] * c for _ in range(r + 3)]
        exit = [[False] * c for _ in range(r + 3)]
        continue
    # print(x, y, " x, y")
    value = exit_logic(x, y)
    # print(value)
    answer += value - 2
    # print(value)

    # for i in graph:
    #     print(i)
    # print()

print(answer)

# for i in graph:
#     print(i)
# c, d

# 6 5 6
# 2 3
# 2 0
# 4 2
# 2 0
# 2 0
# 2 2