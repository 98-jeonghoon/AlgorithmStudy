n = int(input())
arr = [int(input()) for _ in range(n)]
avg = sum(arr) // n
answer = 0

for a in arr:
    if a > avg:
        answer += a - avg

print(answer)