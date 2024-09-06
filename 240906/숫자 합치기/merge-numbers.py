import heapq
n = int(input())

arr = list(map(int, input().split()))
heapq.heapify(arr)

answer = 0
while len(arr) != 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    
    value = a + b
    answer += value
    heapq.heappush(arr, value)
print(answer)