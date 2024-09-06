n = int(input())
A = []
B = []

for _ in range(n):
    value = int(input())
    B.append(value)

answer = 0
for i in range(n):
    if B[i] > n:
        answer += 1

print(answer)