n, k = map(int, input().split())
bomb = []

for _ in range(n):
    bomb.append(int(input()))

answer = -1
seen = set()

# 슬라이딩 윈도우 방식으로 접근
for i in range(n):
    if bomb[i] in seen:
        answer = max(answer, bomb[i])
    seen.add(bomb[i])
    
    # 윈도우 크기 초과 시 앞부분 제거
    if i >= k:
        seen.remove(bomb[i - k])

print(answer if answer != -1 else -1)