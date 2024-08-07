from itertools import combinations

n = int(input())
numbers = list(map(int, input().split()))

min_diff = sum(numbers)

for i in range(1, n):
    for combo in combinations(numbers, i):
        sum_a = sum(combo)
        sum_b = sum(numbers) - sum_a
        diff = abs(sum_a - sum_b)
        min_diff = min(min_diff, diff)

print(min_diff)