'''
Find Duplicates
Description:
Given an array of integers, find and print all duplicates in the array.
Input Format:
The first line contains a single integer n, the size of the array. The second line contains n space-separated integers.
Output Format:
Print all the duplicate integers in the array, space-separated.
Sample Case 1:
Input
8
1 2 3 4 5 2 3 6
Output
2 3

Sample Case 2:
Input:
8
5 1 2 3 5 2 5 4
Output
2 5
'''

import sys
input_data = sys.stdin.read().strip()
def solve (input_data):
    lines = input_data.split("\n")
    n = int (lines [0])
    nums = list (map (int, lines(1).split()))
    seen = []
    repeated_elments = ()
    for i in range (n):
        if nums[i] not in seen:
            seen.append (nums[i])
        else:
            repeated_elments.append(nums[i])
    print (*(sorted (repeated_elments)))

solve (input_data)