import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, weight = map(int, input().split())
    graph[a].append((b, weight))
    graph[b].append((a, weight))

INF = 1e9
distance = [INF] * (n + 1)
path = [-1] * (n + 1)

s, e = map(int, input().split())

distance[s] = 0

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
                path[i[0]] = now

dijkstra(s)

print(distance[e])

path_answer = []
current = e
while current != -1:
    path_answer.append(current)
    current = path[current]

path_answer.reverse()
print(" ".join(map(str, path_answer)))