'''
Longest Subarray with given Sum K(Positives)


Problem Statement: 
Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.
Example 1:
Input:
 nums = [10, 5, 2, 7, 1, 9], k = 15  
Output:
 4  
Explanation:
 The longest sub-array with a sum equal to 15 is [5, 2, 7, 1], which has a length of 4. This sub-array starts at index 1 and ends at index 4, and the sum of its elements (5 + 2 + 7 + 1) equals 15. Therefore, the length of this sub-array is 4.
'''


def longestSubarray(nums, k):
        n = len(nums) 
        maxLength = 0
        for startIndex in range(n):
            for endIndex in range(startIndex, n):
                currentSum = 0
                for i in range(startIndex, endIndex + 1):
                    currentSum += nums[i]

                if currentSum == k:
                    maxLength = max(maxLength, endIndex - startIndex + 1)

        return maxLength