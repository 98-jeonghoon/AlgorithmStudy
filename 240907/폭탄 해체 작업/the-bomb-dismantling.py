n = int(input())
bomb = []

for _ in range(n):
    score, time = map(int, input().split())
    bomb.append((score, time))

bomb.sort(key = lambda x : (x[1], -x[0]))

last_time = 0

answer = 0
for score, time in bomb:
    if time > last_time:
        last_time = time
        answer += score

print(answer)