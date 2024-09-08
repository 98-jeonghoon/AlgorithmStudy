from collections import deque
n = int(input())

arr = []

for _ in range(n):
    x, y = map(int, input().split())
    for _ in range(x):
        arr.append(y)

arr.sort()
arr = deque(arr)
answer = 1e9

while arr:
    answer = min(answer, arr.popleft() + arr.pop())

print(answer)