n = int(input())
nums = []

for _ in range(n):
    x, y = map(int, input().split()) 
    nums.append((y, x)) 

nums.sort()

left = 0 
right = len(nums) - 1 
answer = 0

while left < right:

    pair_sum = nums[left][0] + nums[right][0]
    answer = max(answer, pair_sum)


    pair_count = min(nums[left][1], nums[right][1])
    nums[left] = (nums[left][0], nums[left][1] - pair_count)
    nums[right] = (nums[right][0], nums[right][1] - pair_count)


    if nums[left][1] == 0:
        left += 1
    if nums[right][1] == 0:
        right -= 1

print(answer)