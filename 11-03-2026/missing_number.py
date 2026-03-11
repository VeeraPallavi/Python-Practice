"""
Find the missing number 
Input: arr[] = [8, 2, 4, 5, 3, 7, 1]
Output: 6
Explanation: All the numbers from 1 to 8 are present except 6.

Input: arr[] = [1, 2, 3, 5]
Output: 4
Explanation: Here the size of the array is 4, so the range will be [1, 5]. The missing number between 1 to 5 is 4
"""

class Solution:
    def missing_number(self,nums):
        sum = 0
        for i in nums : 
            sum = sum + i

        n= len(nums)
        actual_sum = ((n+1)*(n+2))/2 

        return actual_sum - sum 
