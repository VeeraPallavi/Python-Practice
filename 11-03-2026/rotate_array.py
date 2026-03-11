"""
Left Rotate an array by one
Example 1:
Input:
 nums = [1, 2, 3, 4, 5]  
Output:
 [2, 3, 4, 5, 1]  
Explanation:
 Initially, nums = [1, 2, 3, 4, 5]  
Rotating once to the left results in nums = [2, 3, 4, 5, 1].

Example 2:
Input:
 nums = [-1, 0, 3, 6]  
Output:
 [0, 3, 6, -1]  
Explanation:
 Initially, nums = [-1, 0, 3, 6]  
Rotating once to the left results in nums = [0, 3, 6, -1]."""

def solve(arr, n):
    temp = [0] * n  

    
    for i in range(1, n):
        temp[i - 1] = arr[i]
    temp[n - 1] = arr[0]  


    for num in temp:
        print(num, end=" ")  