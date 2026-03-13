"""
Input : nums = [1, 2, 3, 4, 5, 6, 7], k = 2, right
Output : [6, 7, 1, 2, 3, 4, 5]
Explanation : rotate 1 step to the right: [7, 1, 2, 3, 4, 5, 6]
rotate 2 steps to the right: [6, 7, 1, 2, 3, 4, 5] 

Input : nums = [1, 2, 3, 4, 5, 6], k=2, left
Output : [3, 4, 5, 6, 1, 2]
Explanation :rotate 1 step to the left: [2, 3, 4, 5, 6, 1]
rotate 2 steps to the left: [3, 4, 5, 6, 1, 2]
"""

class Solution:
    def rotateLeft(self, arr, k):
        n = len(arr)
        if n == 0:
            return
        k %= n
        temp = arr[:k]
        for i in range(k, n):
            arr[i - k] = arr[i]
        for i in range(k):
            arr[n - k + i] = temp[i]