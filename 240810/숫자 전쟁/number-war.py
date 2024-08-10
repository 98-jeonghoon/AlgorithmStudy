def max_score(n, player1, player2):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if player2[j] < player1[i]:
                dp[i][j] = dp[i][j+1] + player2[j]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i+1][j+1])
    
    return dp[0][0]

n = int(input())
player1 = list(map(int, input().split()))
player2 = list(map(int, input().split()))

print(max_score(n, player1, player2))