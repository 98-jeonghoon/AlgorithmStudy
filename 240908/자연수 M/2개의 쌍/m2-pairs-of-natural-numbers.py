n = int(input()) 
nums = [] 


for _ in range(n):
    count, value = map(int, input().split())
    nums.extend([value] * count) 

nums.sort()  

answer = 0  
left = 0  
right = len(nums) - 1  

# 작은 수와 큰 수를 계속 짝지음
while left < right:
    pair_sum = nums[left] + nums[right]  # 두 수의 합
    answer = max(answer, pair_sum)  # 가장 큰 합을 저장
    left += 1  # 작은 수의 인덱스 이동
    right -= 1  # 큰 수의 인덱스 이동

print(answer)