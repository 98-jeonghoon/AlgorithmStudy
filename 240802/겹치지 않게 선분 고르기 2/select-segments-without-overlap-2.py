def max_non_overlapping_segments(n, segments):
    segments.sort(key=lambda x: x[0])
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if segments[i][0] > segments[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)


n = int(input())
segments = []
for _ in range(n):
    x1, x2 = map(int, input().split())
    segments.append((x1, x2))


result = max_non_overlapping_segments(n, segments)
print(result)