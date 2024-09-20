def can_color_half(grid, D):
    N = len(grid)
    total_cells = N * N
    target = (total_cells + 1) // 2  # 반올림
    visited = [[-1] * N for _ in range(N)]
    
    def dfs(x, y, color):
        if visited[x][y] == color:
            return 0
        if visited[x][y] != -1:
            return 0
        
        visited[x][y] = color
        count = 1
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and abs(grid[nx][ny] - grid[x][y]) <= D:
                count += dfs(nx, ny, color)
        
        return count

    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1:
                if dfs(i, j, grid[i][j]) >= target:
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