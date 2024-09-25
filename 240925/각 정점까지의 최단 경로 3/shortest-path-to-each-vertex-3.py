import heapq

n, m = map(int, input().split())
INF = 1e9

# 시작 정점 = 1
start = 1

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

def dijkstra(start):
    queue = []
    # 시작 노드로 가기위한최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        # 만약 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        
        # 현재 노드와 연결된 다른 인접한 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

dijkstra(start)

for i in range(2, n + 1):
    if distance[i] == INF:
        print(-1)
    else:
        print(distance[i])


# print(distance)