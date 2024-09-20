import sys
from collections import deque

def can_color_half(grid, D):
    N = len(grid)
    total_cells = N * N
    target = (total_cells + 1) // 2  # 반올림
    
    def bfs(start_x, start_y):
        visited = [[False] * N for _ in range(N)]
        queue = deque([(start_x, start_y)])
        visited[start_x][start_y] = True
        count = 1
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    if abs(grid[nx][ny] - grid[x][y]) <= D:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        count += 1
                        if count >= target:
                            return True
        return False

    for i in range(N):
        for j in range(N):
            if bfs(i, j):
                return True
    return False

def find_min_D(grid):
    left, right = 0, max(max(row) for row in grid)
    
    while left < right:
        mid = (left + right) // 2
        if can_color_half(grid, mid):
            right = mid
        else:
            left = mid + 1
    
    return left


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]


print(find_min_D(grid))