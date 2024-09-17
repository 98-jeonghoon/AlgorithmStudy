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
while i < C and j < N:
    if black_stones[j][0] <= red_stones[i] <= black_stones[j][1]:
        # 매칭 가능하면 매칭하고 둘 다 인덱스를 증가시킴
        matches += 1
        i += 1
        j += 1
    elif red_stones[i] < black_stones[j][0]:
        # 빨간 돌의 값이 검정 돌의 A보다 작으면 빨간 돌 인덱스 증가
        i += 1
    else:
        # 검정 돌의 B보다 빨간 돌의 값이 크면 검정 돌 인덱스 증가
        j += 1

print(matches)