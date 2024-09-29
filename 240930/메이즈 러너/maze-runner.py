n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = -1

exit_x, exit_y = map(int, input().split())
exit_pos = (exit_x - 1, exit_y - 1)
graph[exit_x - 1][exit_y - 1] = 1e9

def find_exit_pos():
    global exit_pos
    for x in range(n):
        for y in range(n):
            if graph[x][y] == 1e9:
                exit_pos = (x, y)
                return

def is_end():
    # 참가자가 탈출에 성공한다면 -> 참가자가 없다면
    for x in range(n):
        for y in range(n):
            if graph[x][y] < 0:
                return False
    return True

def people_move():
    global answer
    exit_x, exit_y = exit_pos
    new_graph = [[0] * n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            # 만약에 사람이 있다면
            if graph[x][y] < 0:
                is_exit = False
                # 현재 위치와 출구와의 거리
                min_distance = abs(x - exit_x) + abs(y - exit_y)
                min_x, min_y = (-1, -1)
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    # 만약 이동한곳이 탈출구라면
                    if (nx, ny) == exit_pos:
                        is_exit = True
                        answer += 1
                        break
                    # 범위안에 들어가고 벽이 없다면
                    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] <= 0:
                        distance = abs(nx - exit_x) + abs(ny - exit_y)
                        # 만약 이동한게 더 가깝다면
                        if distance < min_distance:
                            min_x, min_y = nx, ny
                            min_distance = distance

                if is_exit == True:
                    continue
                # 이동이 가능하다면 이동하고 거리를 추가해줌
                if (min_x, min_y) != (-1, -1):
                    new_graph[min_x][min_y] += graph[x][y]
                    answer += 1
                # 이동이 불가능하다면 그대로 냅둠
                else:
                    new_graph[x][y] += graph[x][y]
    # 그래프를 최신화해줌
    for x in range(n):
        for y in range(n):
            if graph[x][y] > 0:
                new_graph[x][y] = graph[x][y]

    # for i in new_graph:
    #     print(i)
    return new_graph
def find_square():
    for size in range(2, n):
        for x in range(n - size + 1):
            for y in range(n - size + 1):
                is_people, is_exit = False, False
                for x_size in range(x, x + size):
                    for y_size in range(y, y + size):
                        # print(x_size, y_size)
                        if graph[x_size][y_size] == 1e9:
                            is_exit = True
                            continue
                        if graph[x_size][y_size] < 0:
                            is_people = True
                if is_exit == True and is_people == True:
                    return size, x, y


    pass

def rotate(square_size, square_x, square_y):
    new_graph = [[0] * square_size for _ in range(square_size)]
    for x in range(square_size):
        for y in range(square_size):
            new_graph[x][y] = graph[square_x + x][square_y + y]
    new_graph = list(map(list, zip(*new_graph[::-1])))


    for x in range(square_size):
        for y in range(square_size):
            graph[square_x + x][square_y + y] = new_graph[x][y]

def down_wall(size, x, y):
    for i in range(size):
        for j in range(size):
            if graph[x + i][y + j] != 1e9 and graph[x + i][y + j] > 0:
                graph[x + i][y + j] = max(graph[x + i][y + j] - 1, 0)

for time in range(k):
    if is_end():
        break
    graph = people_move()
    square_size, square_x, square_y = find_square()
    # print(square_size, square_x, square_y)
    rotate(square_size, square_x, square_y)
    down_wall(square_size, square_x, square_y)
    find_exit_pos()
    # for i in graph:
    #     print(i)
    # print()
    pass


print(answer)
print(exit_pos[0] + 1, exit_pos[1] + 1)