k, n = map(int, input().split())

num = [i for i in range(1, k + 1)]

arr = []
answer = 0
def backTracking(depth):
    global answer
    if depth == n:
        print(*arr)
        return
    for i in range(k):
        arr.append(num[i])
        backTracking(depth + 1)
        arr.pop()

backTracking(0)