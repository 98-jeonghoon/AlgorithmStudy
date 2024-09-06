import heapq

n = int(input())
bomb = []

for _ in range(n):
    score, time = map(int, input().split())
    bomb.append((score, time))

# 점수를 기준으로 내림차순 정렬
bomb.sort(key=lambda x: (-x[0], x[1]))

# 시간을 추적하며 사용할 리스트
time_slots = [0] * 10001  # 최대 10,000까지의 시간을 다룰 수 있음

total_score = 0

# 각 폭탄을 점수가 높은 순서대로 처리
for score, time in bomb:
    # 해당 폭탄을 가장 늦게 처리할 수 있는 시간을 찾는다.
    while time > 0 and time_slots[time] != 0:
        time -= 1
    # 남은 시간이 있으면 그 시간대에 폭탄을 처리한다.
    if time > 0:
        time_slots[time] = 1
        total_score += score

print(total_score)