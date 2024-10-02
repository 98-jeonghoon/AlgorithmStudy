from collections import deque

n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
time_graph = [[0] * m for _ in range(n)]

# 우/하/좌/상의 우선순위대로
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def is_end():
    cnt = 0
    for x in range(n):
        for y in range(m):
            # 만약 부서지지 않은 포탑이 1개가 된다면 그 즉시 중지해야됨
            if graph[x][y] != 0:
                cnt += 1
                if cnt >= 2:
                    return False
    return True


def find_attacker(time):
    attacker = []
    for x in range(n):
        for y in range(m):
            if graph[x][y] != 0:
                attacker.append((graph[x][y], time_graph[x][y], x, y))
    attacker.sort(key=lambda x : (x[0], -x[1], -(x[2] + x[3]), -x[3]))
    attacker_x, attacker_y = attacker[0][2], attacker[0][3]
    graph[attacker_x][attacker_y] += (n + m)
    time_graph[attacker_x][attacker_y] = time
    return attacker_x, attacker_y
    pass

def find_victim():
    victim = []
    for x in range(n):
        for y in range(m):
            if (x, y) != (attacker_x, attacker_y) and graph[x][y] != 0:
                victim.append((graph[x][y], time_graph[x][y], x, y))
    victim.sort(key=lambda x : (-x[0], x[1], (x[2] + x[3]), x[3]))
    victim_x, victim_y = victim[0][2], victim[0][3]
    return victim_x, victim_y
    pass

def bfs(x, y, victim_x, victim_y):
    visited = [[False] * m for _ in range(n)]
    backTrace = [[None] * m for _ in range(n)]
    visited[x][y] = True
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = (x + dx[d]) % n
            ny = (y + dy[d]) % m
            if 0 <= nx < n and 0 <= ny < n:
                # 부서진 포탑이 아니고, 방문한 포탑이 아니면
                if graph[nx][ny] != 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    # 어디서 온건지 기록해야됨
                    backTrace[nx][ny] = (x, y)
                    if (nx, ny) == (victim_x, victim_y):
                        return visited, backTrace

    return visited, backTrace

def potan_attack(attacker_x, attacker_y, victim_x, victim_y):
    dxs = [-1, -1, -1, 0, 0, 1, 1, 1]
    dys = [-1, 0, 1, -1, 1, -1, 0, 1]
    graph[victim_x][victim_y] -= graph[attacker_x][attacker_y]
    tracking = [(victim_x, victim_y)]
    for d in range(8):
        nx = (victim_x + dxs[d]) % n
        ny = (victim_y + dys[d]) % m
        if (nx, ny) != (attacker_x, attacker_y):
            graph[nx][ny] -= graph[attacker_x][attacker_y] // 2
            tracking.append((nx, ny))
    return tracking
    pass

def laser_attack(attacker_x, attacker_y, victim_x, victim_y, backTrace):
    # 해당 좌표는 바로 공격
    graph[victim_x][victim_y] -= graph[attacker_x][attacker_y]
    start_x, start_y = victim_x, victim_y
    tracking = [(start_x, start_y)]
    while True:
        next_coordinate = backTrace[start_x][start_y]
        if next_coordinate == (attacker_x, attacker_y):
            return tracking
        start_x, start_y = next_coordinate
        graph[start_x][start_y] -= graph[attacker_x][attacker_y] // 2
        tracking.append((start_x, start_y))

    pass

def destory():
    for x in range(n):
        for y in range(m):
            # 0이하가 된 포탑은 부서짐
            if graph[x][y] < 0:
                graph[x][y] = 0
    pass

def repair(tracking):
    for x in range(n):
        for y in range(m):
            # 공격에 무관하고 부서지지 않았으면
            if (x, y) not in tracking and graph[x][y] != 0:
                graph[x][y] += 1
    pass

def attack(attacker_x, attacker_y, victim_x, victim_y):
    visited, backTrace = bfs(attacker_x, attacker_y, victim_x, victim_y)
    # for i in visited:
    #     print(i)
    # print()
    # for i in backTrace:
    #     print(i)
    # 도달할수 있다면 레이저 공격
    if visited[victim_x][victim_y] == True:
        tracking = laser_attack(attacker_x, attacker_y, victim_x, victim_y, backTrace)
        tracking.append((attacker_x, attacker_y))
        destory()
        repair(tracking)
        # print("lazer")
    else:
        tracking = potan_attack(attacker_x, attacker_y, victim_x, victim_y)
        tracking.append((attacker_x, attacker_y))
        destory()
        repair(tracking)
        # print("potan")

    pass

for time in range(1, k + 1):
    attacker_x, attacker_y = find_attacker(time)
    victim_x, victim_y = find_victim()
    attack(attacker_x, attacker_y, victim_x, victim_y)
    # for i in graph:
    #     print(i)
    # print()
    pass

answer = 0

for x in range(n):
    for y in range(m):
        answer = max(answer, graph[x][y])

print(answer)