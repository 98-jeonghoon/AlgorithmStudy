from itertools import combinations

n = int(input())
arr1 = list(map(int, input().split()))

answer = 1e9

for value in combinations(arr1, n):
    arr2 = arr1.copy()
    for v in value:
        arr2.remove(v)
    
    for value2 in combinations(arr2, n):
        answer = min(answer, abs(sum(value) - sum(value2)))

print(answer)