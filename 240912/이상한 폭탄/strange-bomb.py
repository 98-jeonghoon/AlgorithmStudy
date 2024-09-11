n, k = map(int, input().split())
bomb = []

for _ in range(n):
    bomb.append(int(input()))

answer = -1e9

for i in range(n):
    if i + k < n:
        if bomb[i] == bomb[i + k]:
            answer = max(answer, bomb[i])

print(answer)