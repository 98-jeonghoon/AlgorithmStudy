n, m, k = map(int, input().split())
gun_graph = [[[] for _ in range(n)] for _ in range(n)]
init_graph = [list(map(int, input().split())) for _ in range(n)]
people_graph = [[0] * n for _ in range(n)]
people = [[] for _ in range(m + 1)]
have_gun = [0] * (m + 1)
score = [0] * (m + 1)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(1, m + 1):
    x, y, d, s = map(int, input().split())
    people_graph[x - 1][y - 1] = i
    people[i] = [x - 1, y - 1, d, s]

for x in range(n):
    for y in range(n):
        if init_graph[x][y] != 0:
            gun_graph[x][y].append(init_graph[x][y])

def change_dir(direct):
    if direct in [0, 1]:
        return direct + 2
    else:
        return direct - 2

def fight(first, second):
    first_stat, second_stat = people[first][3], people[second][3]
    first_gun, second_gun = have_gun[first], have_gun[second]
    score_calc = abs((first_stat + first_gun) - (second_stat + second_gun))
    if first_stat + first_gun > second_stat + second_gun:
        score[first] = score_calc
        return first, second

    if first_stat + first_gun < second_stat + second_gun:
        score[second] = score_calc
        return second, first

    if (first_stat + first_gun) == (second_stat + second_gun):
        if first_stat > second_stat:
            score[first] = score_calc
            return first, second
        else:
            score[second] = score_calc
            return second, first
    pass

def loser_move(x, y, loser_idx):
    # step 2-2-2 : 진 플레이어는 가지고 있는 총을 격자에 내려놓고, 플레이어가 가지고 있던 방향대로 한칸 이동한다
    if have_gun[loser_idx] != 0:
        # 진칸에 총을 내려둠
        gun_graph[x][y].append(have_gun[loser_idx])
        have_gun[loser_idx] = 0
    loser_direct = people[loser_idx][2]
    while True:
        nx = x + dx[loser_direct]
        ny = y + dy[loser_direct]
        # 만약 이동하려는 칸이 범위 밖이거나 다른 플레이어가 있다면
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            if people_graph[nx][ny] != 0:
                # 90도 회전
                loser_direct = (loser_direct + 1) % 4
                continue
        else:
            # 그게 아니라면 해당 칸으로 이동하고, 만약 해당 칸에 총이 있다면 가장 공격력이 높은 총 획득
            # 사람의 좌표를 바꿔줌
            people[loser_idx][0], people[loser_idx][1], people[loser_idx][2] = nx, ny, loser_direct

            # 총줍기
            if gun_graph[nx][ny]:
                gun_graph[nx][ny].sort()
                have_gun[loser_idx] = gun_graph[nx][ny].pop()

            return


    pass

def check_is_people(x, y, nx, ny, idx):
    # step 2-1 : 이동한 방향에 플레이어가 없다면 총이 있는지 확인하고 총이 있는 경우 총 획득
    # 이미 총을 가지고 있다면 놓여있는 총들과 플레이어가 가진 총중 공격력이 가장 큰 총 획득
    # 만약에 이동한 칸에 사람이 없다면, 이동한 칸에 내가 있다면(제자리 이동이 아니라면)
    if people_graph[nx][ny] == 0 and people_graph[nx][ny] != idx:
        # 칸에 총이 있다면
        if gun_graph[nx][ny]:
            # 만약 총을 가지고 있지 않다면
            if have_gun[idx] == 0:
                gun_graph[nx][ny].sort()
                have_gun[idx] = gun_graph[nx][ny].pop()
            # 가지고 있으면 내려두고 정렬한다음 다시 집음
            else:
                gun_graph[nx][ny].append(have_gun[idx])
                gun_graph[nx][ny].sort()
                have_gun[idx] = gun_graph[nx][ny].pop()
        # 사람의 위치랑 사람 그래프의 값을 바꿔줌
        people[idx][0], people[idx][1] = nx, ny


    # 이동한 곳에 사람이 있다면
    else:
        # step 2-2-1 : 두 플레이어가 싸운다. 해당 플레이어의 초기 능력치와 가지고 있는 총의 공격력의 합을 비교
        first_player = idx
        second_player = people_graph[nx][ny]
        winner, loser = fight(first_player, second_player)

        # step 2-2-2 : 진 플레이어는 가지고 있는 총을 격자에 내려놓고, 플레이어가 가지고 있던 방향대로 한칸 이동한다
        loser_move(nx, ny, loser)
        people[winner][0], people[winner][1] = nx, ny
        # step 2-2-3
        if have_gun[winner] != 0:
            gun_graph[nx][ny].append(have_gun[winner])
            have_gun[winner] = 0
            gun_graph[nx][ny].sort()
            have_gun[winner] = gun_graph[nx][ny].pop()
        # return True

def people_move():
    global people_graph
    # step 1-1 : 플레이어가 순차적으로 본인이 향하고 있는 방향대로 한 칸 이동한다
    # if 격자를 벗어나는 경우 정반대 방향으로 바꾸어서 이동
    for idx in range(1, m + 1):
        x, y, d, s = people[idx][0], people[idx][1], people[idx][2], people[idx][3]
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            direct = change_dir(d)
            people[idx][2] = direct
            nx = x + dx[direct]
            ny = y + dy[direct]
            check_is_people(x, y, nx, ny, idx)
            people_graph = [[0] * n for _ in range(n)]
            for iii in range(1, m + 1):
                people_x, people_y, people_d, people_s = people[iii]
                people_graph[people_x][people_y] = iii
            continue
        check_is_people(x, y, nx, ny, idx)
        people_graph = [[0] * n for _ in range(n)]
        for i in range(1, m + 1):
            people_x, people_y, people_d, people_s = people[i]
            people_graph[people_x][people_y] = i



for _ in range(k):
    people_move()
    # for i in people_graph:
    #     print(i)
    # print()
    # print(have_gun)
    # print()
    # print(people)
    # print("-------------------------")
print(*score[1:])