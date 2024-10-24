from itertools import combinations

n = int(input())
graph = [input() for _ in range(n)]

# 동전 번호에 따른 위치 저장용 딕셔너리
coin_pos = {}
start_pos = (0, 0)
end_pos = (0, 0)

# 입력을 받아서 좌표 저장
for x in range(n):
    for y in range(n):
        if graph[x][y] == "S":
            start_pos = (x, y)
        elif graph[x][y] == "E":
            end_pos = (x, y)
        else:
            try:
                num = int(graph[x][y])
                coin_pos[num] = (x, y)
            except ValueError:
                continue

# 동전 번호를 정렬하여 순서대로 수집할 수 있게 한다.
coins = sorted(coin_pos.keys())
answer = 1e9

# 최소 3개부터 최대 모든 동전을 선택하여 순열을 구한다.
for cnt in range(3, len(coins) + 1):
    for value in combinations(coins, cnt):
        dist = 0
        now = start_pos

        # 선택된 동전 순서대로 이동
        for coin in value:
            next_pos = coin_pos[coin]
            dist += abs(now[0] - next_pos[0]) + abs(now[1] - next_pos[1])
            now = next_pos

        # 마지막으로 도착지까지의 거리 추가
        dist += abs(now[0] - end_pos[0]) + abs(now[1] - end_pos[1])
        answer = min(answer, dist)

if answer == 1e9:
    print(-1)
else:
    print(answer)