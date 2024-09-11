n, k = map(int, input().split())
bomb = []

for _ in range(n):
    bomb.append(int(input()))

answer = -1e9

for i in range(n):
    if i + k < n:
        if bomb[i] == bomb[i + k]:
            answer = max(answer, bomb[i])

if answer == -1e9:
    print(-1)
else:
    print(answer)