import sys
from collections import deque

# 변수 선언 및 입력:
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dxs = [1, -1,  0, 0]
dys = [0,  0, -1, 1]

# bfs를 이용해 색칠하고 몇 칸이 칠해졌는지 확인합니다.
def bfs(start_x, start_y, d):
    visited = [[False] * n for _ in range(n)]
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    count = 1

    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            next_x, next_y = x + dx, y + dy
            if (0 <= next_x < n and 0 <= next_y < n
                and not visited[next_x][next_y]
                and abs(board[next_x][next_y] - board[x][y]) <= d):
                visited[next_x][next_y] = True
                queue.append((next_x, next_y))
                count += 1

    return count

# d 이하로 인접한 칸을 색칠한다고 할 때,
# 색칠된 칸이 전체 칸의 반 이상이 될 수 있는지 판단합니다.
def is_possible(d):
    for i in range(n):
        for j in range(n):
            if bfs(i, j, d) * 2 >= n * n:
                return True
    return False

lo = 0                       # 답이 될 수 있는 가장 작은 숫자 값을 설정합니다.
hi = 1000000                 # 답이 될 수 있는 가장 큰 숫자 값을 설정합니다.
ans = 0                      # 답을 저장합니다.

while lo <= hi:              # [lo, hi]가 유효한 구간이면 계속 수행합니다.
    mid = (lo + hi) // 2     # 가운데 위치를 선택합니다.
    if is_possible(mid):     # 결정문제에 대한 답이 Yes라면
        hi = mid - 1         # 왼쪽에 조건을 만족하는 숫자가 더 있을 가능성 때문에 hi를 바꿔줍니다.
        ans = mid            # 답의 후보들 중 최댓값을 계속 갱신해줍니다.
    else:
        lo = mid + 1         # 결정문제에 대한 답이 No라면 lo를 바꿔줍니다.

# 정답을 출력합니다.
print(ans)