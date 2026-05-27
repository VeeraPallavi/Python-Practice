'''
Repeat and Missing Number Array
Description
You are given a read-only array of n intefers from 1 to n.
Each integer appears exactly one, except for: A, wjich apperas twice, and B, which is missing.
Your task is to return the two integers, A and B. The value of A should precede B in the ouput.
your algorithm should have a linear runtime complexity O(n) and should not use xtra memory.

Input Format:
The first line contains an integer n.
The second line contains n integers, representing the elements of the array.
Output Format:
Print an array containing the two integers [A,B].

Sample Case 1:
Input:
5
3 1 2 5 3
Output:
[3, 4]
'''

import sys

input_data = sys.stdin.read().strip()

def solve(input_data):
    lines = input_data.split("\n")
    n = int(lines[0].split())
    nums = list(map(int,lines[1].split()))

    actual_Sum = n*(n+1)//2
    actual_square_sum = n*(n+1)*(2*n+1)//6

    expected_sum = sum(nums)
    expected_square_sum = sum(x*x for x in nums)

    S = actual_Sum-expected_sum
    P = actual_square_sum-expected_square_sum

    sum_AB = P//S

    missing = (S+sum_AB)//2
    repeated = missing - S

    print(f"[{repeated}, {missing}]")

solve(input_data) 