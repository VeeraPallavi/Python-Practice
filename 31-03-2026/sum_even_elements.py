'''
Sum of Even Elements
Description
Given an array of integers of size N, print the sum of all even elements present in the array.
Input Format
The first line contains an integer N, the size of the array. The second line contains N space-separated integers representing the array elements.
Output Format
Print the sum of all even elements present in the array.
Sample Case 1
Input
5
1 2 3 4 5
Output
6
'''

import sys

# Read input from standard input

input_data = sys.stdin.read().strip()

def solve (input_data):
    lines = input_data.split("\n") # Split input int
    # User writes their logic here
    n = int (lines[0])
    nums = list (map(int, lines [1].split()))
    even_sum = 0
    for i in nums:
        if i % 2 == 0:
            even_sum = even_sum +i
    print(even_sum)
#Call the function
solve (input_data)