n = int(input())
arr = list(map(int, input().split()))

def dp_logic(arr):
    n = len(arr)
    
    # LIS 계산
    lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                lis[i] = max(lis[i], lis[j] + 1)
    
    # LDS 계산 (앞에서부터)
    lds = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] < arr[j]:
                lds[i] = max(lds[i], lds[j] + 1)
    
    # 최장 증가-감소 부분 수열 길이 계산
    max_length = 0
    for i in range(n):
        max_length = max(max_length, lis[i] + lds[i] - 1)
    
    return max_length

print(dp_logic(arr))