def max_non_overlapping_segments(n, segments):
    segments.sort(key=lambda x: x[1])

    count = 0
    last_end = -1

    for start, end in segments:
        # 현재 선분의 시작점이 이전 선분의 끝점보다 크면 선택
        if start > last_end:
            count += 1
            last_end = end

    return count


n = int(input())
segments = []
for _ in range(n):
    x1, x2 = map(int, input().split())
    segments.append((x1, x2))

result = max_non_overlapping_segments(n, segments)
print(result)