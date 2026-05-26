'''
Rotate Array
Dscription
Given an array, rotate the array to thr right by k steps, where k is non-negative.
Input Format:
The first line contains two integers n (1 ≤ n ≤ 10^5) and k(1 ≤ k ≤ 10^5). 
The second line contains n integers, representing the elements of the array.
Output Format:
Print the roated array.
Sample Case 1:
Input:
7 3
1 2 3 4 5 6 7
Output:
5 6 7 1 2 3 4'''

import sys

input_data = sys.stdin.read().strip()

def solve(input_data):
    lines = input_data.split("\n")
    values = list(map(int,lines[0].split()))
    n,k = values[0],values[1]
    nums = list(map(int,lines[1].split()))
    
    k = k%n
    nums[:] = nums[:-k]+nums[:-k]

    print(*nums)

solve(input_data)