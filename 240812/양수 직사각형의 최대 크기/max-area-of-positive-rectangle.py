n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def find_square(x, y, xx, yy):
    for i in range(x, xx + 1):
        for j in range(y, yy + 1):
            if graph[i][j] <= 0:
                return -1
    else:
        value = (xx - x + 1) * (yy - y + 1)
        return value
    


answer = -1



for x in range(n):
    for y in range(m):
        if graph[x][y] > 0:
            for xx in range(x, n):
                for yy in range(y, m):
                    answer = max(answer, find_square(x, y, xx, yy))

print(answer)