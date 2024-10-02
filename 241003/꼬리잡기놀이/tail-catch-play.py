n, m, k = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def find_team():
    head = []
    for x in range(n):
        for y in range(n):
            # 머리가 1 꼬리가 3
            if graph[x][y] == 1:
                head.append((x, y))

    teammates = []

    for head_x, head_y in head:
        x, y = head_x, head_y
        team = []
        team.append((x, y))
        while graph[x][y] != 3:
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                # 범위를 벗어나면 안됨
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                # 머리 다음 이동한곳이 꼬리이면 안됨
                if graph[x][y] == 1 and graph[nx][ny] == 3:
                    continue
                # 0으로 이동하면 안됨
                if graph[nx][ny] == 0:
                    continue
                # 4로 이동하면 안됨
                if graph[nx][ny] == 4:
                    continue
                # 다시 돌아오면 안됨
                if (nx, ny) in team:
                    continue

                team.append((nx, ny))
                x, y = nx, ny
                break
        teammates.append(team)
    # print(teammates)
    return teammates

def teams_move(teams):
    move_teams = []

    # 머리만 이동시켜주면, 나머지는 그 뒤에 것 그대로 넣으면 이동끝
    for team in teams:
        head = team[0]
        head_x, head_y = head[0], head[1]
        move_team = []
        for d in range(4):
            nx = head_x + dx[d]
            ny = head_y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 4 or graph[nx][ny] == 3:
                    move_team.append((nx, ny))
                    break
        move_team.extend(team[:len(team) - 1])
        move_teams.append(move_team)
    return move_teams
    pass

def renewal_graph(teams, move_teams):
    # 움직일 수 있는 칸으로 바꿔주고
    for team in teams:
        for x, y in team:
            graph[x][y] = 4

    for move_team in move_teams:
        for idx in range(len(move_team)):
            # 머리인 친구
            if idx == 0:
                graph[move_team[idx][0]][move_team[idx][1]] = 1
                continue
            # 맨 마지막인 친구
            if idx == len(move_team) - 1:
                graph[move_team[idx][0]][move_team[idx][1]] = 3
                continue
            graph[move_team[idx][0]][move_team[idx][1]] = 2
    pass

answer = 0
# 7 * 4 = 28
def throws_ball_pos(round):
    # 초기 좌표를 상, 하, 좌, 우로 설정함
    # x, y, 방향을 리턴할거임
    total = n * 4
    # 0 ~ 6
    if 0 <= round % total < n:
        return round % total, 0, 3
    # 7 ~ 13 -> 0, 1, 2, 3, 4, 5, 6
    if n <= round % total < 2 * n:
        return n - 1, round % total % n, 0
    # 14 ~ 20 -> 6 5 4 3 2 1 0
    if 2 * n <= round % total < 3 * n:
        return (3 * n) - round % total - 1, n - 1, 2
    # 21 -> 27 -> 6 5 4 3 2 1 0
    if 3 * n <= round % total < 4 * n:
        return 0, (4 * n) - round % total - 1, 1
    pass

def find_bump_people(ball_x, ball_y, direct):
    while True:
        # 범위를 벗어나면
        if ball_x < 0 or ball_y < 0 or ball_x >= n or ball_y >= n:
            return False, -1, -1
        if 1 <= graph[ball_x][ball_y] <= 3:
            return True, ball_x, ball_y
        ball_x += dx[direct]
        ball_y += dy[direct]

def cnt_point_reverse(bump_x, bump_y):
    global answer
    # 팀들 전체를 돌면서
    for move_team in move_teams:
        # 해당 팀에 부딪힌 애가 있다면
        if (bump_x, bump_y) in move_team:
            cnt = 0
            for idx in range(len(move_team)):
                # 몇번째인지 카운트해주기 위함
                if (bump_x, bump_y) == move_team[idx]:
                    # 몇번째인지 카운트했으면 바로 멈추고
                    cnt = idx + 1
                    break
            answer += cnt ** 2
            # 앞대가리랑 뒷대가리랑 바꿔줌
            head_x, head_y = move_team[0][0], move_team[0][1]
            tail_x, tail_y = move_team[-1][0], move_team[-1][1]
            graph[head_x][head_y] = 3
            graph[tail_x][tail_y] = 1
            break



    pass

for round in range(k):
    teams = find_team()
    move_teams = teams_move(teams)
    renewal_graph(teams, move_teams)
    # print(teams)
    # print()
    # print(move_teams)
    # print(round)
    # for i in graph:
    #     print(i)

    ball_x, ball_y, ball_direct = throws_ball_pos(round)
    # print(ball_x, ball_y, ball_direct)
    is_bump, bump_x, bump_y = find_bump_people(ball_x, ball_y, ball_direct)
    if is_bump:
        cnt_point_reverse(bump_x, bump_y)
    # print("round", round, " : ", x, y, direct)
    # print(round)
    # for i in graph:
    #     print(i)

print(answer)