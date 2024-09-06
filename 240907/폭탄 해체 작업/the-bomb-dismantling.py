import heapq

n = int(input())
bomb = []

for _ in range(n):
    score, time = map(int, input().split())
    bomb.append((time, score))

# 시간을 기준으로 오름차순 정렬
bomb.sort()

# 최대 힙을 사용하여 해체할 폭탄 점수를 관리
max_heap = []
total_score = 0

for time, score in bomb:
    # 우선 해체할 폭탄의 점수를 최대 힙에 추가
    heapq.heappush(max_heap, -score)
    
    # 시간이 초과되지 않도록 관리 (해체할 수 있는 시간 내에서만 처리)
    if len(max_heap) > time:
        heapq.heappop(max_heap)  # 점수가 가장 낮은 폭탄은 해체하지 않음

# 남아 있는 폭탄 점수 합산
total_score = -sum(max_heap)

print(total_score)