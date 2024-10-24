from itertools import combinations

n = int(input())
arr1 = list(map(int, input().split()))

answer = 1e9
for value in combinations(arr1, n):
    arr2 = []
    for i in arr1:
        if i not in value:
            arr2.append(i)
    for value2 in combinations(arr2, n):
        answer = min(abs(sum(value) - sum(value2)), answer)

print(answer)