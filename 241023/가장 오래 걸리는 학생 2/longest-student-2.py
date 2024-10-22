import heapq
n, m = map(int, input().split())

INF = 1e9
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, d = map(int, input().split())
    graph[b].append((a, d))

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            # 가는 거리가 더 짧으면
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

start = n
dijkstra(start)
print(max(distance[1:]))