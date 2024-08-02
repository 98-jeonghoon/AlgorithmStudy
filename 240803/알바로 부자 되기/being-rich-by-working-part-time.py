n = int(input())

arr = []
dp = [0] * n

for i in range(n):
    s, e, p = map(int, input().split())
    arr.append((s, e, p))

arr.sort(key = lambda x:(x[0], x[1], -x[2]))

for i in range(n):
    dp[i] = arr[i][2]  # 현재 작업만 선택하는 경우
    for j in range(i):
        if arr[i][0] > arr[j][1]:  # 겹치지 않는 경우
            dp[i] = max(dp[i], dp[j] + arr[i][2])

print(max(dp))