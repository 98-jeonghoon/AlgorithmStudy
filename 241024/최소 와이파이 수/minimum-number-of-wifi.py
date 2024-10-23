n, m = map(int, input().split())
positions = list(map(int, input().split()))

# 사람들이 사는 위치 리스트 생성 (1부터 시작하므로 인덱스에 1 더하기)
people_positions = [i + 1 for i in range(n) if positions[i] == 1]

count = 0  # 필요한 와이파이 수
i = 0      # 현재 처리 중인 사람의 인덱스

while i < len(people_positions):
    # 현재 사람의 위치
    s = people_positions[i]

    # s로부터 거리 m 이내에 있는 가장 먼 사람의 위치 찾기
    t = s
    while i < len(people_positions) and people_positions[i] <= s + m:
        t = people_positions[i]
        i += 1

    # 와이파이를 위치 t에 설치
    # 이제 위치 t로부터 거리 m 이내의 사람들을 커버해야 함
    x = t
    while i < len(people_positions) and people_positions[i] <= x + m:
        i += 1

    # 와이파이 설치했으므로 카운트 증가
    count += 1

print(count)