n = int(input())

meeting = []

for _ in range(n):
    start, end = map(int, input().split())
    meeting.append((start, end))

meeting.sort(key=lambda x: x[1])

answer = 0
endtime = -1
for start, end in meeting:
    if start >= endtime:
        answer += 1
        endtime = end

print(answer)