C, N = map(int, input().split())

red_stones = []
for _ in range(C):
    red_stones.append(int(input()))

black_stones = []
for _ in range(N):
    a, b = map(int, input().split())
    black_stones.append((a, b))

red_stones.sort()
black_stones.sort(key=lambda x: x[1])

count = 0
j = 0

for i in range(C):
    while j < N and black_stones[j][1] < red_stones[i]:
        j += 1
    
    if j < N and black_stones[j][0] <= red_stones[i] <= black_stones[j][1]:
        count += 1
        j += 1

print(count)