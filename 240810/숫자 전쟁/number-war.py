def max_score(n, player1, player2):
    # DP 테이블 초기화
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # 뒤에서부터 DP 테이블 채우기
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            # 카드 대결
            if player2[j] < player1[i]:
                dp[i][j] = max(dp[i][j], dp[i][j+1] + player2[j])
            else:
                dp[i][j] = max(dp[i][j], dp[i+1][j])
            
            # 카드 버리기
            dp[i][j] = max(dp[i][j], dp[i+1][j+1])
    
    return dp[0][0]

# 입력 받기
n = int(input())
player1 = list(map(int, input().split()))
player2 = list(map(int, input().split()))

# 결과 출력
print(max_score(n, player1, player2))