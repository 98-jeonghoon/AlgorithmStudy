from collections import deque

l, n, q = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(l)]
knight_graph = [[0] * l for _ in range(l)]
knight = [[] for _ in range(n + 1)]
is_dead = [False] * (n + 1)
dmg = [0] * (n + 1)


for idx in range(1, n + 1):
    r, c, h, w, k = map(int, input().split())
    knight[idx] = [idx, r - 1, c - 1, h, w, k]

    for height in range(h):
        knight_graph[r + height - 1][c - 1] = idx
    for weight in range(w):
        knight_graph[r - 1][c + weight - 1] = idx

command = []

for _ in range(q):
    i, d = map(int, input().split())
    command.append((i, d))

# 위 오 아 왼
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def move_knight(idx, direct):
    queue = deque()
    # 기사들의 방문횟수 체크
    visited = [False] * (n + 1)
    visited[idx] = True
    queue.append(idx)
    move_record = [[] for _ in range(n + 1)]

    while queue:
        idx = queue.popleft()
        r, c, h, w = knight[idx][1], knight[idx][2], knight[idx][3], knight[idx][4]

        for row in range(r, r + h):
            for col in range(c, c + w):
                nx = row + dx[direct]
                ny = col + dy[direct]

                # 만약 범위 밖이거나 벽을만난다면 아무 일도 일어나지 않음
                if not 0 <= nx < l or not 0 <= ny < l or graph[nx][ny] == 2:
                    return [], False

                # 이동해야할 곳을 record에 저장함
                move_record[idx].append((nx, ny))

                # 다른 기사를 만났을때
                if knight_graph[nx][ny] != 0 and visited[knight_graph[nx][ny]] == False:
                    queue.append(knight_graph[nx][ny])
                    visited[knight_graph[nx][ny]] = True

    return move_record, True

    pass

def move_knight_graph(record):
    new_knight_graph = [[0] * l for _ in range(l)]
    for idx in range(1, n + 1):
        if len(record[idx]) > 0:
            for nx, ny in record[idx]:
                new_knight_graph[nx][ny] = idx
            r, c = record[idx][0]
            knight[idx][1], knight[idx][2] = r, c
    return new_knight_graph
    pass


for i, direct in command:
    # 만약 사라진 기사에게 명령을 내리면 아무런 반응이 없게된다
    if is_dead[i] == True:
        continue

    record, is_moved = move_knight(i, direct)
    # print(record, is_moved)
    # 움직일 수 있는경우
    if is_moved == True:
        # 데미지를 계산함
        for idx in range(1, n + 1):
            if len(record[idx]) > 0:
                for nx, ny in record[idx]:
                    # 만약 함정이 있고, 명령받은 기사가 아니라면
                    if graph[nx][ny] == 1 and idx != i:
                        dmg[idx] += 1
                        # print(knight)
                        knight[idx][5] -= 1

                        # 체력이 다 깎였으면
                        if knight[idx][5] == 0:
                            is_dead[idx] = True
                            record[idx] = []
                            break

        # 나이트 그래프를 옮겨주기
        knight_graph = move_knight_graph(record)

answer = 0
for idx in range(1, n + 1):
    if is_dead[idx] == False:
        answer += dmg[idx]
print(answer)