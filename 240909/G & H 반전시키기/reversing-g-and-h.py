n = int(input())
start = input().strip()
target = input().strip()

count = 0
i = 0

while i < n:
    if start[i] != target[i]:
        count += 1
        while i < n and start[i] != target[i]:
            i += 1
    else:
        i += 1

print(count)