'''
Find Minimum in Rotated Sorted Array
Dscription
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
Given the sorted rotated array nums of unique elements, return the minimum element of this array. You must write an algorithm that runs in O(log n) time.
Input Format:
The first line contains an integer n(1 <= n <= 5000).
The second lie contains n integers representing the elements of the array.
Output Format:
Prinat a single integer representing the minimum element of the otated array.

Sample Case 1:
Input:
5
3 4 5 1 2
Output:
1

Sample Case 2:
Input:
7
4 5 6 7 0 1 2
Output: 
0
'''

import sys

input_data = sys.stdin.read().strip()

def solve(input_data):
    lines = input_data.split("\n")
    n = int(lines[0].split())
    nums = list(map(int,lines[1].split()))

    left = 0
    right = n-1
    while(left <= right):
        mid = (left+right)//2
        if left == right:
            print(nums[left])
            return
        elif nums[mid]> nums[right]:
            left = mid+1
        else:
            right = mid
        

solve(input_data)