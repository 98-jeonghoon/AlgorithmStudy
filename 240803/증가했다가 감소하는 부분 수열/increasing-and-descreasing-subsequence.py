n = int(input())
arr = list(map(int, input().split()))

def dp_logic(arr):
    n = len(arr)
    
    # LIS 계산
    lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    
    # LDS 계산 (뒤에서부터)
    lds = [1] * n
    for i in range(n-2, -1, -1):
        for j in range(n-1, i, -1):
            if arr[i] > arr[j] and lds[i] < lds[j] + 1:
                lds[i] = lds[j] + 1
    
    # 최장 증가-감소 부분 수열 길이 계산
    max_length = 0
    for i in range(n):
        max_length = max(max_length, lis[i] + lds[i] - 1)
    
    return max_length

print(dp_logic(arr))