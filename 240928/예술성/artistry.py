from collections import deque
from itertools import combinations

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def rotate_cross():
    new_graph = [[0] * n for _ in range(n)]
    rotate_graph = list(map(list, zip(*graph)))[::-1]
    for x in range(n):
        for y in range(n):
            if x == n // 2 or y == n // 2:
                new_graph[x][y] = rotate_graph[x][y]
            else:
                new_graph[x][y] = graph[x][y]
    return new_graph

def rotate_squre():
    # 1D rotate
    new_graph = [[0] * (n // 2) for _ in range(n // 2)]
    for x in range(n // 2):
        for y in range(n // 2):
            new_graph[x][y] = graph[x][y]
    new_graph = list(map(list, zip(*new_graph[::-1])))
    for x in range(n // 2):
        for y in range(n // 2):
            graph[x][y] = new_graph[x][y]

    # 2D rotate
    new_graph = [[0] * (n // 2) for _ in range(n // 2)]
    for x in range(n // 2):
        for y in range((n // 2) + 1, n):
            new_graph[x][y - (n // 2) - 1] = graph[x][y]
    new_graph = list(map(list, zip(*new_graph[::-1])))
    for x in range(n // 2):
        for y in range((n // 2) + 1, n):
            graph[x][y] = new_graph[x][y - (n // 2) - 1]

    # 3D rotate
    new_graph = [[0] * (n // 2) for _ in range(n // 2)]
    for x in range((n // 2) + 1, n):
        for y in range(n // 2):
            new_graph[x - (n // 2) - 1][y] = graph[x][y]
    new_graph = list(map(list, zip(*new_graph[::-1])))
    for x in range((n // 2) + 1, n):
        for y in range(n // 2):
            graph[x][y] = new_graph[x - (n // 2) - 1][y]


    # 4D rotate
    new_graph = [[0] * (n // 2) for _ in range(n // 2)]
    for x in range((n // 2) + 1, n):
        for y in range((n // 2) + 1, n):
            new_graph[x - (n // 2) - 1][y - (n // 2) - 1] = graph[x][y]
    new_graph = list(map(list, zip(*new_graph[::-1])))
    for x in range((n // 2) + 1, n):
        for y in range((n // 2) + 1, n):
            graph[x][y] = new_graph[x - (n // 2) - 1][y - (n // 2) - 1]


    # for i in graph:
    #     print(i)
    pass

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def calc_group(x, y, now):
    grouping = []
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    grouping.append((x, y))
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == False and graph[nx][ny] == now:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    grouping.append((nx, ny))

    return grouping

def calc(group_1, group_2):
    # (a 그룹의 칸수 + b 그룹의 칸수) * 그룹 a의 숫자 값
    calc_value = (len(group_1) + len(group_2)) * graph[group_1[0][0]][group_1[0][1]] * graph[group_2[0][0]][group_2[0][1]]
    # print(calc_value)

    touch = 0
    # 4방향을 확인해서 다른 그룹에 그게 들어가있는지 판별하면됨
    for x, y in group_1:
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if (nx, ny) in group_2:
                    touch += 1

    return calc_value * touch


answer = 0

for k in range(4):
    group = []
    visited = [[False] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if visited[x][y] == False:
                group.append(calc_group(x, y, graph[x][y]))

    group_idx = []
    for i in range(len(group)):
        group_idx.append(i)

    value = 0

    for group_1, group_2 in combinations(group_idx, 2):
        value += calc(group[group_1], group[group_2])

    # print(value)
    answer += value
    if k == 3:
        break
    graph = rotate_cross()
    rotate_squre()
    # for i in graph:
    #     print(i)

print(answer)