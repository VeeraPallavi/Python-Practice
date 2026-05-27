'''
Trapping Rain Water
Description
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
Input Format:
The first line contains an integer n(1<=n<=2X10^4).
The second line contains n non-negative integers representing the elevation map.
Output Format:
print a single integer representing the total units of trapped rainwater.

Sample Case 1:
Input:
12
0 1 0 2 1 0 1 3 2 1 2 1
Output:
6

Sample Case 2:
Input:
6
4 2 0 3 2 5
Output:
9
'''

import sys

input_data = sys.stdin.read().strip()

def solve(input_data):
    lines = input_data.split("\n")
    n = int(lines[0].split())
    nums = list(map(int,lines[1].split()))
    
    leftMax = [0]*n
    rightMax = [0]*n

    leftMax[0] = nums[0]
    for i in range(1,n):
        leftMax[i]=max(leftMax[i-1],nums[i])

    rightMax[0] =  nums[n-1]
    for i in range(n-2,-1,-1):
        rightMax[i]=max(rightMax[i+1], nums[i])

    water = 0 
    for i in range(n):
        water += min(leftMax[i],rightMax[i])-nums[i]

    print(water)

solve(input_data)
