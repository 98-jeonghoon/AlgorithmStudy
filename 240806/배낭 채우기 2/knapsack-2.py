n, m = map(int, input().split())
items = []

for _ in range(n):
    w, v = map(int, input().split())
    items.append((w, v))

# DP 배열 초기화 (1차원)
dp = [0] * (m + 1)

# 각 무게에 대해
for w in range(1, m + 1):
    # 모든 아이템을 고려
    for weight, value in items:
        # 현재 아이템을 선택할 수 있는 경우
        if weight <= w:
            # 이전 상태와 현재 아이템을 선택한 경우 중 최대값 선택
            dp[w] = max(dp[w], dp[w - weight] + value)

# 최대 가치 출력
print(dp[m])