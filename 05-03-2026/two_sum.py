'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''

def two_sum (nums,target):
    arr = [-1, -1]
    for i in range(len(nums) - 1):
        if nums[i] + nums[i + 1] == target:
            arr[0] = i
            arr[1] = i + 1
    
    return arr

nums = list(map(int,input("Enter the numbers: ").split()))
target = int(input("Enter target value"))
print(two_sum(nums,target))