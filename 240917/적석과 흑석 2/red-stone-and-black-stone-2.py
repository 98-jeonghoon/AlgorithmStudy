C, N = map(int, input().split())


red_stones = []
for _ in range(C):
    red_stones.append(int(input()))


black_stones = []
for _ in range(N):
    A, B = map(int, input().split())
    black_stones.append((A, B))

red_stones.sort()
black_stones.sort(key=lambda x: x[1])  

# 투 포인터 방식으로 매칭
i, j = 0, 0  # i는 빨간 돌 인덱스, j는 검정 돌 인덱스
matches = 0
used_reds = set()  # 이미 매칭된 빨간 돌들을 추적

while j < N:
    # 가능한 빨간 돌을 찾는 과정
    while i < C and (red_stones[i] < black_stones[j][0] or i in used_reds):
        i += 1
    # 매칭이 가능하면 매칭 수행
    if i < C and black_stones[j][0] <= red_stones[i] <= black_stones[j][1]:
        matches += 1
        used_reds.add(i)
        i += 1
    j += 1

print(matches)