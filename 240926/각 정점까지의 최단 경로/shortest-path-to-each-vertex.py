import heapq

n, m = map(int, input().split())
start = int(input())

INF = 1e9
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

distance[start] = 0

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        dist, now = heapq.heappop(queue)
        # 처리된 노드면 무시
        if distance[now] < dist:
            continue
        
        # 현재 노드와 연결된 다른 노드를 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))
        

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print(-1)
    else:
        print(distance[i])