'''
Sum of Extremes
Description:
Given an array of integers, your task is to find and print the sum of the largest and smallest elements in the array.
Input Format:
The first line contains a single integer 'n', representing the number of elements in the array. The second line contains `n space-separated integers, representing the elements of the array.
Output Format:
Print a single integer, the sum of the largest and smallest elements in the array.
Sample Case 1
Input:
5
1 2 3 4 5
Output:
6
'''

import sys
input_data = sys.stdin.read().strip()
def solve (input_data):
    lines = input_data.split("\n")
    n = int(lines[0])
    nums = list(map(int, lines[0].split()))
    max_element = max(nums)
    smallest_element = min(nums)
    print(max_element + smallest_element)

solve(input_data)