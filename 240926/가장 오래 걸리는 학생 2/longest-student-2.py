import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
INF = 1e9

distance = [INF] * (n + 1)

start = n

for _ in range(m):
    i, j, d = map(int, input().split())
    graph[j].append((i, d))

distance[start] = 0

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

dijkstra(start)
print(max(distance[1:]))