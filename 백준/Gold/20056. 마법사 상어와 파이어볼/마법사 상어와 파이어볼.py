n, m, k = map(int, input().split())
fire_ball = []

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

graph = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    # fire_ball.append((r - 1, c - 1, m, s, d))
    graph[r - 1][c - 1].append((m, s, d))

def debug_graph():
    for i in graph:
        print(i)

def move_fire_ball():
    new_graph = [[[] for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            while graph[x][y]:
                m, s, d = graph[x][y].pop()
                nx = (x + dx[d] * s) % n
                ny = (y + dy[d] * s) % n
                new_graph[nx][ny].append((m, s, d))

    return new_graph

def two_more():
    new_graph = [[[] for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            # 같은 칸에 있는 파이어볼은 모두 합쳐진다.
            # 만약 칸에 파이어볼이 하나인경우
            if len(graph[x][y]) == 1:
                new_graph[x][y].append((graph[x][y].pop()))
            # 그게 아니라 2개 이상일 경우
            else:
                # 해당 칸에 있는 모든 파이어볼이 하나로 합쳐진다
                total_m, total_s, odd_cnt, even_cnt, fire_ball_cnt = 0, 0, 0, 0, len(graph[x][y])
                while graph[x][y]:
                    m, s, d = graph[x][y].pop()
                    total_m += m
                    total_s += s
                    if d % 2 == 0:
                        even_cnt += 1
                    else:
                        odd_cnt += 1
                m_L = total_m // 5
                # 만약 질량이 0인 파이어볼은 소멸
                if m_L == 0:
                    continue
                s_L = total_s // fire_ball_cnt
                # 만약 합쳐지는 파이어볼 방향이 모두 홀수이거나 모두 짝수이면
                if odd_cnt == 0 or even_cnt == 0:
                    direct = [0, 2, 4, 6]
                else:
                    direct = [1, 3, 5, 7]
                # 파이어볼 나누기
                for d in direct:
                    new_graph[x][y].append((m_L, s_L, d))

    return new_graph

for _ in range(k):
    graph = move_fire_ball()
    graph = two_more()

answer = 0
for x in range(n):
    for y in range(n):
        if graph[x][y]:
            for m, s, d in graph[x][y]:
                answer += m

print(answer)

# debug_graph()