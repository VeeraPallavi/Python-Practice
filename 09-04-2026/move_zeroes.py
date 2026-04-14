'''
Move Zeroes
Description:
A chocolate factory is packing chocolates into packets. The chocolate packets here represent an array of N integer values. The task is to find the empty packets (0) of chocolate and push them to the end of the conveyor belt (array). A
Input Format:
First line contains an integer n, representing size of an array. Second line contains n space separated integer values.
Output Format:
The output is the array with all zeros moved to the end, while maintaining the order of non-zero elements.
Sample Case 1:
Input:
8 
4 5 0 1 9 0 5 0
Output
4 5 1 9 5 0 0 0
'''

import sys
input_data = sys.stdin.read().strip()
def solve (input_data):
    lines = input_data.split("\n")
    n = int (lines[0])
    nums = list (map(int, lines [1].split()))
    pos = 0
    for i in range(n):
        if nums[i] != 0:
            nums [pos] = nums[i]
            pos += 1
    for i in range (pos, n):
        nums [i]=0 
        pos += 1
    print(*nums)

solve (input_data)