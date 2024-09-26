n, m, h, k = map(int, input().split())
runner = []
tree_graph = [[False] * n for _ in range(n)]
is_dead = [False] * m
sulae_pos = (n // 2, n // 2)

# 정방향인지 역방향인지 확인하는 변수
now_direct = True
runner_graph = [[[] for _ in range(n)] for _ in range(n)]
# 좌우상하
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

# 상 우 하 좌
tornado_dx = [-1, 0, 1, 0]
tornado_dy = [0, 1, 0, -1]

for idx in range(m):
    x, y, d = map(int, input().split())
    runner.append((x - 1, y - 1, d))
    runner_graph[x - 1][y - 1].append(idx)

for _ in range(h):
    x, y = map(int, input().split())
    tree_graph[x - 1][y - 1] = True

direct_graph = [[0] * n for _ in range(n)]
reverse_direct_graph = [[0] * n for _ in range(n)]

def reverse_direct(direct):
    if direct in [0, 1]:
        return direct + 2
    else:
        return direct - 2


def tornado_graph():
    x, y = n // 2, n // 2
    direct = 0
    dist = 1
    cnt = 0
    while True:
        for i in range(dist):
            direct_graph[x][y] = direct
            nx = x + tornado_dx[direct]
            ny = y + tornado_dy[direct]
            if (nx, ny) == (-1, 0):
                return
            r_direct = reverse_direct(direct)
            reverse_direct_graph[nx][ny] = r_direct
            x, y = nx, ny

        direct = (direct + 1) % 4
        cnt += 1
        if cnt == 2:
            cnt = 0
            dist += 1
    pass

tornado_graph()

def change_runner_direct(direct):
    if direct in [1, 3]:
        return direct - 1
    else:
        return direct + 1

def runner_move(x, y, direct, runner_idx):
    nx = x + dx[direct]
    ny = y + dy[direct]
    # 만약 격자 벗어나지 않는경우
    if 0 <= nx < n and 0 <= ny < n:
        # 술래가 있으면
        if (nx, ny) == sulae_pos:
            # 움직이지 않는다
            return
        # 술래가 없으면 움직임
        else:
            runner[runner_idx] = (nx, ny, direct)
            return
    # 격자에서 벗어나면
    else:
        # 반대방향으로 틀어주고
        chg_direct = change_runner_direct(direct)
        # 다시 방향이로 이동해봄
        nx = x + dx[chg_direct]
        ny = y + dy[chg_direct]
        # 술래가 없다면 이동
        if (nx, ny) != sulae_pos:
            runner[runner_idx] = (nx, ny, chg_direct)
            return

def sulae_move():
    global sulae_pos, now_direct
    x, y = sulae_pos
    # 만약 정방향 이동이면
    if now_direct == True:
        nx = x + tornado_dx[direct_graph[x][y]]
        ny = y + tornado_dy[direct_graph[x][y]]
        sulae_pos = (nx, ny)
        # 만약 0, 0에 도착하면 바로 역방향 그래프로 바꿔줌
        if (nx, ny) == (0, 0):
            now_direct = False
    else:
        nx = x + tornado_dx[reverse_direct_graph[x][y]]
        ny = y + tornado_dy[reverse_direct_graph[x][y]]
        sulae_pos = (nx, ny)
        if (nx, ny) == (n // 2, n // 2):
            now_direct = True

    pass


def catch_runner(t):
    global answer
    x, y = sulae_pos
    if now_direct == True:
        for s in range(3):
            nx = x + tornado_dx[direct_graph[x][y]] * s
            ny = y + tornado_dy[direct_graph[x][y]] * s
            if 0 <= nx < n and 0 <= ny < n:
                # 만약 해당칸에 나무가 없으면
                if tree_graph[nx][ny] == False:
                    # 점수계산
                    answer += t * len(runner_graph[nx][ny])
                    for runner_idx in runner_graph[nx][ny]:
                        # 러너 죽이고
                        is_dead[runner_idx] = True
                        # 그래프도 비워줌
                        runner_graph[nx][ny] = []
    else:
        for s in range(3):
            nx = x + tornado_dx[reverse_direct_graph[x][y]] * s
            ny = y + tornado_dy[reverse_direct_graph[x][y]] * s
            if 0 <= nx < n and 0 <= ny < n:
                if tree_graph[nx][ny] == False:
                    answer += t * len(runner_graph[nx][ny])
                    for runner_idx in runner_graph[nx][ny]:
                        is_dead[runner_idx] = True
                        runner_graph[nx][ny] = []



    pass

def runner_graph_init():
    global runner
    new_runner_graph = [[[] for _ in range(n)] for _ in range(n)]
    for idx in range(m):
        if is_dead[idx]:
            continue
        runner_x, runner_y, runner_d = runner[idx]
        new_runner_graph[runner_x][runner_y].append(idx)
    return new_runner_graph

    pass

answer = 0

for t in range(1, k + 1):
    # 도망자가 먼저 움직임
    for idx in range(m):
        # 죽은 러너면 무시
        if is_dead[idx]:
            continue
        runner_x, runner_y, runner_d = runner[idx]
        if abs(runner_x - sulae_pos[0]) + abs(runner_y - sulae_pos[1]) <= 3:
            runner_move(runner_x, runner_y, runner_d, idx)
    runner_graph = runner_graph_init()
    # print(runner)
    sulae_move()
    catch_runner(t)
    # print(sulae_pos)

# for i in direct_graph:
#     print(i)
# print()
# for i in reverse_direct_graph:
#     print(i)

print(answer)