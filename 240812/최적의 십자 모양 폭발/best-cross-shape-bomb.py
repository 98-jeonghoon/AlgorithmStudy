import copy

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def count_pair(copy_graph):
    count = 0
    for x in range(n):
        for y in range(n):
            if copy_graph[x][y] == 0:
                continue
            now_value = copy_graph[x][y]
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    if copy_graph[nx][ny] == now_value:
                        count += 1
    return count // 2

    pass

def gravity(copy_graph):
    # 첫번재 부터
    for y in range(n):
        # 아래쪽부터
        for x in range(n - 2, -1, -1):
            if copy_graph[x][y] == 0:
                continue
            value = copy_graph[x][y]
            now_x = x
            while True:
                # 만약 끝점에 도달했거나, 0이 아닌 숫자가 있으면 멈춤
                if now_x + 1 >= n or copy_graph[now_x + 1][y] != 0:
                    break
                now_x += 1
            copy_graph[x][y] = 0
            copy_graph[now_x][y] = value

    return copy_graph

def explosion(x, y, copy_graph):
    # 선택된 숫자 값
    select_num = copy_graph[x][y]
    copy_graph[x][y] = 0
    # 숫자 값만큼 터트려야함
    for d in range(4):
        for s in range(select_num):
            nx = x + dx[d] * s
            ny = y + dy[d] * s
            if 0 <= nx < n and 0 <= ny < n:
                copy_graph[nx][ny] = 0

    # print(select_num)
    # print("--------------------------------------")
    # for i in copy_graph:
    #     print(i)
    # print()
    # 중력작용하기
    copy_graph = gravity(copy_graph)
    # for i in copy_graph:
    #     print(i)
    # print()
    # print("--------------------------------------")
    count = count_pair(copy_graph)
    return count

answer = -1


copy_graph = [
    [0 for _ in range(n)]
    for _ in range(n)
]
# 완탐으로 모든 좌표 다 폭탄 터트려보기
for x in range(n):
    for y in range(n):
        # 원본 그래프를 바꾸면 안됨
        
        for i in range(n):
            for j in range(n):
                copy_graph[i][j] = graph[i][j]
        answer = max(answer, explosion(x, y, copy_graph))

print(answer)