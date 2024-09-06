n = int(input())
arr = list(map(int, input().split()))

answer = 0
past_min_value = 1e9

for i in range(n):
    past_min_value = min(arr[i], past_min_value)
    answer = max(arr[i] - past_min_value, answer)

print(answer)