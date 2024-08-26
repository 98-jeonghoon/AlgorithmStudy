from collections import deque

answer = []

k, m = map(int, input().split())
n = 5

graph = [list(map(int, input().split())) for _ in range(n)]
numbers = list(map(int, input().split()))
numbers = deque(numbers)

dxs = [-1, -1, -1, 0, 0, 1, 1, 1]
dys = [-1, 0, 1, -1, 1, -1, 0, 1]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 유물가치 최대화, 회전 각도가 가장 작은 방법, 중심 좌표ㅕ의 열이 가장작은, 행의 가장 작은

def create_new_maze(x, y):
    mid_x, mid_y = x, y
    new_maze = [[0] * 3 for _ in range(3)]
    direct_queue = deque()
    for d in range(8):
        nx = x + dxs[d]
        ny = y + dys[d]
        direct_queue.append((nx, ny))

    cnt = 0

    for i in range(3):
        for j in range(3):
            # 만약 중앙값좌표라면
            if (i, j) == (1, 1):
                new_maze[i][j] = graph[x][y]
                continue
            new_x, new_y = direct_queue[cnt]
            new_maze[i][j] = graph[new_x][new_y]
            cnt += 1

    # for i in new_maze:
    #     print(i)
    # print()

    return new_maze

def rotate(new_maze, rotate_cnt):
    for i in range(rotate_cnt):
        new_maze = list(map(list, zip(*new_maze[::-1])))
    return new_maze
    pass

def attach_maze(maze, x, y):
    new_graph = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_graph[i][j] = graph[i][j]

    attach = deque()

    for i in range(3):
        for j in range(3):
            if (i, j) == (1, 1):
                continue
            attach.append(maze[i][j])

    # 새로운 그래프의 가운데 좌표는 회전한 그래프의 가운데 좌표이다
    new_graph[x][y] = maze[1][1]
    for d in range(8):
        nx = x + dxs[d]
        ny = y + dys[d]
        new_graph[nx][ny] = attach.popleft()

    # for i in new_graph:
    #     print(i)
    # print()

    # 이제 해당 그래프를 바탕으로 유물 획득을 해야함
    return new_graph

def get_treasure(x, y, now):
    visited[x][y] = True
    queue = deque()
    queue.append((x, y))

    treasure_arr = []
    treasure_arr.append((x, y))

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == False and new_graph[nx][ny] == now:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    treasure_arr.append((nx, ny))

    if len(treasure_arr) >= 3:
        return treasure_arr
    else:
        return None


    pass

# def search():
#     for x in range(1, n - 1):
#         for y in range(1, n - 1):
#             # 격자칸 하나를 선택해서 회전시켜야함
#             # 1회전, 2회전, 3회전
#             new_maze = create_new_maze(x, y)
#             for cnt in range(1, 4):
#                 rotate_maze = rotate(new_maze, cnt)
#                 # 회전 한것을 그래프에 가져다 붙여야함
#                 new_graph = attach_maze(rotate_maze, x, y)
#                 get_treasure(new_graph)
#     pass


def bfs(x, y, now):
    visited[x][y] = True
    queue = deque()
    queue.append((x, y))

    treasure_arr = []
    treasure_arr.append((x, y))

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == False and graph[nx][ny] == now:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    treasure_arr.append((nx, ny))

    if len(treasure_arr) >= 3:
        return treasure_arr
    else:
        return None

for i in range(k):
    check = []
    for x in range(1, n - 1):
        for y in range(1, n - 1):
            # 격자칸 하나를 선택해서 회전시켜야함
            # 1회전, 2회전, 3회전
            new_maze = create_new_maze(x, y)
            for cnt in range(1, 4):
                rotate_maze = rotate(new_maze, cnt)
                # 회전 한것을 그래프에 가져다 붙여야함
                new_graph = attach_maze(rotate_maze, x, y)
                # 해당 그래프를 바탕으로 유물 획득 로직 진행
                visited = [[False] * n for _ in range(n)]
                treasure = []
                for new_x in range(n):
                    for new_y in range(n):
                        if visited[new_x][new_y] == False:
                            get = get_treasure(new_x, new_y, new_graph[new_x][new_y])
                            if get != None:
                                treasure.extend(get)
                if treasure != []:
                    check.append((len(treasure), cnt, x, y, treasure))
    check.sort(key= lambda x : (-x[0], x[1], x[3], x[2]))
    if check == []:
        break
    else:
        # 회전수, x, y 좌표를 기준으로 가장 다시 graph 회전해서 돌리기
        rotate_cnt, rotate_x, rotate_y = check[0][1], check[0][2], check[0][3]
        new_new_maze = create_new_maze(rotate_x, rotate_y)
        rotate_new_maze = rotate(new_new_maze, rotate_cnt)
        graph = attach_maze(rotate_new_maze, rotate_x, rotate_y)
        remove = check[0][4]
        cnt = check[0][0]
        while True:
            remove.sort(key=lambda x : (x[1], -x[0]))
            for remove_x, remove_y in remove:
                graph[remove_x][remove_y] = numbers.popleft()

            visited = [[False] * n for _ in range(n)]
            remove = []
            for i in range(n):
                for j in range(n):
                    if visited[i][j] == False:
                        get_arr = bfs(i, j, graph[i][j])
                        if get_arr != None:
                            remove.extend(get_arr)
            if remove == []:
                break
            else:
                cnt += len(remove)
        answer.append(cnt)
print(*answer)