from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS로 D 값이 주어졌을 때 색칠할 수 있는 칸의 개수를 구하는 함수
def bfs(N, grid, D, start_x, start_y, visited):
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    count = 1  # 시작 칸도 포함
    base_value = grid[start_x][start_y]
    
    while queue:
        x, y = queue.popleft()
        
        # 상하좌우로 이동 가능한지 확인
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 격자 밖으로 나가지 않도록 하고, 아직 방문하지 않았는지 확인
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                # 숫자 차이가 D 이하인 경우에만 이동 가능
                if abs(grid[nx][ny] - base_value) <= D:
                    visited[nx][ny] = True
                    count += 1
                    queue.append((nx, ny))
    
    return count

# 색칠 가능한 칸이 전체 칸의 절반 이상인지 확인하는 함수
def can_paint_half(N, grid, D):
    visited = [[False] * N for _ in range(N)]
    target = (N * N + 1) // 2  # 절반 이상을 칠해야 하는 최소 칸 수
    
    # 모든 칸에서 시작하여 확인해본다.
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                # 한 번 BFS 돌려서 색칠할 수 있는 칸 수를 확인한다.
                count = bfs(N, grid, D, i, j, visited)
                if count >= target:
                    return True
    
    return False

# 이분 탐색으로 D 값을 찾는 함수
def find_min_D(N, grid):
    low, high = 0, 1000000  # D의 가능한 최소값과 최대값
    result = high
    
    while low <= high:
        mid = (low + high) // 2
        if can_paint_half(N, grid, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return result


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

print(find_min_D(N, grid))