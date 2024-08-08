n = int(input())
numbers = list(map(int, input().split()))

total_sum = sum(numbers)

# 두 그룹으로 나눌 수 있는지 확인
if total_sum % 2 != 0:
    print("No")
else:
    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in numbers:
        for j in range(target, num - 1, -1):
            if dp[j - num]:
                dp[j] = True

    # 적어도 하나의 요소를 포함하는 두 그룹으로 나눌 수 있는지 확인
    if dp[target] and any(dp[target - num] for num in numbers):
        print("Yes")
    else:
        print("No")