n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# print(graph)

visited = [False] * (n + 1)
answer = 0


def dfs(start):
    global answer
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            answer += 1
            dfs(i)
    pass

dfs(1)
print(answer)