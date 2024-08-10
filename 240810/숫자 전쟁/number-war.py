import sys

sys.setrecursionlimit(2000)  # 재귀 제한을 늘려줍니다.

def solve(a, b):
    if a == n or b == n:
        return 0

    if dp[a][b] != -1:
        return dp[a][b]

    if player1[a] < player2[b]:
        dp[a][b] = solve(a + 1, b)

    if player1[a] > player2[b]:
        dp[a][b] = max(dp[a][b], solve(a, b + 1) + player2[b])

    dp[a][b] = max(dp[a][b], solve(a + 1, b + 1))

    return dp[a][b]

def max_score():
    n = int(input().strip())
    global player1, player2, dp
    player1 = list(map(int, input().strip().split()))
    player2 = list(map(int, input().strip().split()))

    # dp 테이블 초기화
    dp = [[-1] * n for _ in range(n)]

    # 결과 계산
    ans = solve(0, 0)
    print(ans)

max_score()