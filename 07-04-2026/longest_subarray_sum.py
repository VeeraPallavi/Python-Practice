'''Find the maximum sum of a contiguous subarray'''

def max_subarray(nums):
    max_sum = current = nums[0]
    
    for num in nums[1:]:
        current = max(num, current + num)
        max_sum = max(max_sum, current)
    
    return max_sum

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))