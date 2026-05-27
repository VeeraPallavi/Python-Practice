'''
Longest Subarrat with sum Divisible by K
Description
Given an array arr[] containin n integers and a positive integer k, find the longset subarray's length where the sum f elemnts is divisible by the given value k.
Input Format:
The fist line cotains two integers n and k(1 ≤ n ≤ 10^5,  1 ≤ k ≤ 10^9).
The second line contains n space-seperated inteers representing the elements of the array.
Output Format:
Print a single integer, the length of the longest subarray.

Sample Case 1
Input:
6 3 
2 7 6 1 4 5
Output:
4

Sample Case 2:
Input 
7 3
-2 2 -5 12 -11 -1 7
Output:
5
'''

import sys

input_data = sys.stdin.read().strip()

def solve(input_data):
    lines = input_data.split("\n")

    n,k = map(int,lines[0].split())
    nums = list(map(int,lines[1].split()))

    sum, max_count = 0, 0
    for length in range(n,0,-1):
        for i in range(0,n-length+1):
            sum = 0
            for j in range(i,i+length):
                sum += nums[j]
            if sum % k == 0:
                max_count = max(max_count,length)
    print(max_count)

solve(input_data)