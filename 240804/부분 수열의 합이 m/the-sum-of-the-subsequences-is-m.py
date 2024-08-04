n, m = map(int, input().split())
arr = list(map(int, input().split()))

from itertools import combinations

combs = []
for i in range(n):
    for comb in combinations(arr, i):
        combs.append(comb)
        if sum(comb) == m:
            print(len(comb))
            exit(0)
else:
    print(-1)