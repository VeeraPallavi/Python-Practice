'''
Count Greater Elements
Description
Given an integer array of size N, count the number of elements where each element is greater than all of its preceding elements. The first element should always be included in the count.
Input Format
The first line contains an integer N, the number of items. Second line contains n space separated integer representing the value of the array elements.
Output Format
Print the count of elements that are greater than all preceding elements.
Sample Case 1
Input
5
7 4 8 2 9
Output:
3
'''


import sys

# Read input from standard input

input_data = sys.stdin.read().strip()

def solve (input_data):
    lines = input_data.split("\n") # Split input int
    # User writes their logic here
    n = int (lines[0])
    nums = list (map(int, lines [1].split()))
    count = 1
    max_value = nums[0]
    for i in range(1, n):
        if nums[i] > max_value:
            count += 1
            max_value = nums[i]
    print(count)
#Call the function
solve (input_data)