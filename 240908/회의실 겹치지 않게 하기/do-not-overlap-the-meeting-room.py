n = int(input())
meeting = []

visited = [False] * n

for _ in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))

meeting.sort(key=lambda x : x[1])


last_time = -1
answer = 0
for s, e in meeting:
    if s >= last_time:
        answer += 1
        last_time = e

print(n - answer)