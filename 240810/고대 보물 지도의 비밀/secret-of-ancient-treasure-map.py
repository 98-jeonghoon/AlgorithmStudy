def max_sum_with_limited_negatives(n, k, numbers):
    left = 0
    current_sum = 0
    max_sum = 0
    negative_count = 0

    for right in range(n):
        current_sum += numbers[right]
        
        if numbers[right] < 0:
            negative_count += 1
        
        while negative_count > k:
            if numbers[left] < 0:
                negative_count -= 1
            current_sum -= numbers[left]
            left += 1
        
        max_sum = max(max_sum, current_sum)

    return max_sum

n, k = map(int, input().split())
numbers = list(map(int, input().split()))

print(max_sum_with_limited_negatives(n, k, numbers))