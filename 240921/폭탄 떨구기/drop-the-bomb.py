N, K = map(int, input().split())
points = [int(input()) for _ in range(N)]

points.sort()

def can_remove_all_with_R(R):
    bombs_used = 0
    i = 0

    while i < N:
        bombs_used += 1
        start = points[i]  # 현재 폭탄을 떨어뜨릴 시작점
        # 이 폭탄으로 R 범위 내에 있는 점들을 모두 제거
        while i < N and points[i] <= start + 2 * R:
            i += 1

        # 폭탄을 K번 초과해서 사용하면 False
        if bombs_used > K:
            return False

    return True

left, right = 0, 1000000000
answer = right

while left <= right:
    mid = (left + right) // 2

    if can_remove_all_with_R(mid):
        answer = mid  # 가능한 R 값 중 최소값을 찾는다
        right = mid - 1
    else:
        left = mid + 1


print(answer)