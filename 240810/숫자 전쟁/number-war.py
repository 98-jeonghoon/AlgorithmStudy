def max_score():
    import sys
    
    input = sys.stdin.readline
    
    n = int(input().strip())
    player1 = list(map(int, input().strip().split()))
    player2 = list(map(int, input().strip().split()))

    # 동적 계획법 테이블 초기화
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # 카드 정렬
    player1.sort()
    player2.sort()

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if player2[j - 1] < player1[i - 1]:
                dp[i][j] = max(dp[i - 1][j - 1] + player2[j - 1], dp[i - 1][j], dp[i][j - 1])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    print(dp[n][n])

max_score()