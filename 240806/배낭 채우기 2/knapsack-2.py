n = int(input())
sticks = [(0, 0)]
arr = list(map(int, input().split()))
for i in range(1, n + 1):
    sticks.append((i, arr[i - 1]))

dp = [[0] * (n + 1) for _ in range(n + 1)]

# 길이 먼저 시작
for length in range(1, n + 1):
    for stick in range(1, n + 1):
        stick_len, stick_value = sticks[stick]
        #  선택된 길이로 현재 길이를 만들 수 없다면
        if stick_len > length:
            # 전에 것 그대로 가져옴
            dp[length][stick] = dp[length][stick - 1]
        else:
            if length % stick_len == 0:
                quotient = length // stick_len
                dp[length][stick] = max(dp[length][stick - 1], stick_value * quotient)
                continue
            dp[length][stick] = max(dp[length][stick - 1], dp[length - stick_len][stick - 1] + stick_value)

print(dp[n][n])