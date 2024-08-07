n, m = map(int, input().split())


quests = [tuple(map(int, input().split())) for _ in range(n)]

INF = float('inf')
max_exp = sum(e for e, t in quests) 
dp = [INF] * (max_exp + 1)
dp[0] = 0  

for e, t in quests:
    for j in range(max_exp, e - 1, -1):
        if dp[j - e] != INF:
            dp[j] = min(dp[j], dp[j - e] + t)
min_time = min(dp[m:])

if min_time == INF:
    print(-1)
else:
    print(min_time)