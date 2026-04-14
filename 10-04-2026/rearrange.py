'''
Rearrange 0s, 1s, 2s
Description:
Given an integer array/list containing only Os, 1s, and 2s, sort the array in a single scan. The array should be sorted in non-decreasing order, where all Os come first, followed by all 1s, and then all 2s.
Input Format:
The first line contains an integer T, the number of test cases. Each test case starts with an integer N, the size of the array/list, followed by N integers (Os, 1s, and 2s) representing the elements of the array/list.
Output Format:For each test case, print the sorted array on a new line.
Sample Case 1
Input:
2
6
0 1 2 2 1 0
7
0 1 2 1 2 1 2
Output:
0 0 1 1 2 2
0 1 1 1 2 2 2
'''
import sys
input_data = sys.stdin.read().strip()
def solve (input_data):
    lines = input_data.split("\n")
    T = int(lines[0])
    index = 1
    for i in range(T):
        N = int(lines[index])
        nums = list(map(int,lines[index+1].split()))
        index += 2
        for j in range(N-1):
            for k in range(i+1, N):
                if nums[j] > nums[k]:
                    nums[j], nums[k] = nums[k], nums[j]
        print(*nums)

solve(input_data)