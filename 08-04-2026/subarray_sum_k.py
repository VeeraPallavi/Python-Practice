'''Count subarrays whose sum equals k'''

def subarray_sum(nums, k):
    count = 0
    n = len(nums)
    
    for i in range(n):
        current_sum = 0
        
        for j in range(i, n):
            current_sum += nums[j]
            
            if current_sum == k:
                count += 1
    
    return count

print(subarray_sum([1, 1, 1], 2))