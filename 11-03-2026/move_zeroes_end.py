"""
Move Zeroes to end

Input: 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
Output: 1 ,2 ,3 ,4 ,1 ,0 ,0 ,0
Explanation: All the zeros are moved to the end and non-negative integers are moved to front by maintaining order
Input : 1,2,0,1,0,4,0
Output: 1,2,1,4,0,0,0
Explanation : All the zeros are moved to the end and non-negative integers are moved to front by maintaining order

"""

class Solution:
    def moveZeroes(self, nums):
        j = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                break
        if j == -1:
            return

        for i in range(j + 1, len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
sol = Solution()
nums = [1,2,0,1,0,4,0]
sol.moveZeroes(nums)

print(" ".join(map(str, nums)))
