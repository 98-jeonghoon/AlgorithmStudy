n = int(input())
arr = list(map(int, input().split()))

mid_arr = []
for i in range(n):
    mid_arr.append(arr[i])
    if len(mid_arr) % 2 == 1:
        mid_arr.sort()
        print(mid_arr[len(mid_arr) // 2], end=" ")