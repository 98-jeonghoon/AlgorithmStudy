n = int(input())
A = []
B = []

for _ in range(n):
    value = int(input())
    B.append(value)

for i in range(1, n * 2 + 1):
    if i not in B:
        A.append(i)

A.sort()
B.sort()

A_pointer = 0
B_pointer = 0
answer = 0
while True:
    if A_pointer == n:
        break
    if A[A_pointer] > B[B_pointer]:
        answer += 1
        A_pointer += 1
        B_pointer += 1
    else:
        A_pointer += 1

print(answer)