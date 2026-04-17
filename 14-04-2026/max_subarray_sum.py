'''
Max Subarray Sum
Description:
Write a program that takes an integer n and an array of n integers as Input and returns the contiguous subarray with the largest sum along with the sum.
Input Format:
The input consists of an integer 'n followed by an array of n integers, where 1 <= n <= 1000 and -10000 <= nums[i] <= 10000
Output Format:
The output consists of the largest sum and the subarray that produces this sum.
Sample Case 1
Input:
9 
-2 1 -3 4 -1 2 1 -5 4
Output
6
4 -1 2 1
'''
import sys
input_data = sys.stdin.read().strip()
def solve (input_data):
    lines = input_data.split("\n")
    n=int (lines[0])
    nums = list (map (int, lines [1].split()))

    max_sum = float('-inf')
    current_sum = 0
    start = 0
    end = 0
    temp_start = 0
    for i in range(n) :
        current_sum += nums[i]
        if current_sum >= max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
        if current_sum < 0:
            current_sum = 0
            temp_start = i+1
    print(max_sum)
    print(*nums[start:end+1])

solve(input_data)
