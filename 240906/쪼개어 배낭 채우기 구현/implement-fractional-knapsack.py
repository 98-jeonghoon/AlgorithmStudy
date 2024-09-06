n, m = map(int, input().split())
knapsack = []

for _ in range(n):
    w, v = map(int, input().split())
    knapsack.append((w, v, v / w))  # 가치 대 무게 비율을 저장

# 가치 대 무게 비율이 높은 순서대로 정렬
knapsack.sort(key=lambda x: -x[2])

total_weight = m
answer = 0.0

for w, v, w_v in knapsack:
    if total_weight >= w:
        # 보석을 전부 담을 수 있는 경우
        total_weight -= w
        answer += v
    else:
        # 보석의 일부만 담을 수 있는 경우
        answer += (total_weight / w) * v
        break

print(f"{answer:.3f}")