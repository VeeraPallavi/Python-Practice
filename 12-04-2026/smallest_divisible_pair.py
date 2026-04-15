'''
Smallest Divisible Pair
Description:
Given an array of integers and a single integer k, find the pair of elements in the array that, when added together and divided by k, results in the smallest Integer value. If no valid pair exists, return -1.
Input Format:
First line contains size of an array
Second line contains n space separated integer values
Third line contains k value
Output Format
If a valid pair exists, output the pair of integers that results in the smallest value when their sum is divided by k. If no valid pair exists, output-1.
Sample Case 1
Input:
5
8 4 5 7 9
3
Output
4 5
'''
import sys
input_data = sys.stdin.read().strip()
def solve (input_data):
    lines = input_data.split("\n")
    n = int (lines [0])
    nums = list (map (int, lines [1].split()))
    k = int (lines [2])
    smallest_pair = [-1, -1]
    smallest_sum = float('inf')
    found = True
    for i in range (0, n-1):
        for j in range(1+1, n):
            res = (nums[i]+nums[j])%k
            if res == 0:
                if smallest_sum > (nums[i] + nums[j]):
                    smallest_sum = nums[i]+nums[j]
                    smallest_pair[0] = nums[i]
                    smallest_pair[1] =nums[j]
                    found = False
    if found:
        print("-1")
    else:
        print(*smallest_pair)

solve(input_data)