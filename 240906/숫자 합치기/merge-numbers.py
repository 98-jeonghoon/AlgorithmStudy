n = int(input())

arr = list(map(int, input().split()))

answer = 0
while len(arr) != 1:
    arr.sort(reverse=True)
    value = arr.pop() + arr.pop()
    answer += value
    arr.append(value)
print(answer)