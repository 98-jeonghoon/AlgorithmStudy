from itertools import combinations

def get_max_xor(n, m, nums):
    max_xor = 0
    for comb in combinations(nums, m):
        xor_result = 0
        
        for num in comb:
            xor_result ^= num
        
        max_xor = max(max_xor, xor_result)
    
    return max_xor


n, m = map(int, input().split())
nums = list(map(int, input().split()))


print(get_max_xor(n, m, nums))