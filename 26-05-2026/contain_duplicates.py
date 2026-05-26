'''
Contains Duplicate
Description:
Given an integer array nums, retum true if any value appears at least twice in the array, and retum false if every element is distinct.
Input Format:
The first line contains an integer n (1 ≤ n ≤ 10^5). 
The second line contains n integers, representing the elements of the array.
Output Format:
Print true if any value appears at least twice; otherwise, print false.

Sample Case 1
Input
4
1 2 3 1
Output
true

Sample Case 2

Input
4
1 2 3 4
Output
false
'''
import sys

input_data = sys.stdin.read().strip()

def solve(input_data):
    lines = input_data.split("\n")
    n = lines[0]
    nums = list(map(int,lines[1].split()))
    for i in nums:
        if nums.count(i) != 1:
            print("true")
            return
    print("false")

solve(input_data)