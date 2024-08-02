n = int(input())

arr = []
dp = [0] * n

for i in range(n):
    s, e, p = map(int, input().split())
    arr.append((s, e, p))
    dp[i] = p

arr.sort(key = lambda x:(x[0], x[1], -x[2]))

for i in range(1, n):
    for j in range(i):
        if arr[i][0] > arr[j][1]:
            dp[i] = max(dp[i], dp[j] + arr[j][2])

print(max(dp))
# print(arr)