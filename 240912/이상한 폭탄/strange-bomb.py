n, k = tuple(map(int, input().split()))
arr = [
    int(input())
    for _ in range(n)
]
R = [0] * n
last = [-1 for _ in range(1000001)]

for i in range(n - 1, -1, -1):
    R[i] = last[arr[i]]
    last[arr[i]] = i

ans = -1
for i in range(n):
    if R[i] != -1 and R[i] - i <= k:
        ans = max(ans, arr[i])

print(ans)