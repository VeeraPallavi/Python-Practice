'''
Even Numbers Array
Description:
Write a program to print even numbers present in an array.
Input Format:
First line contains a single integer N. Next line contains N space separated integer values.
Output Format:
Print space separated even integer values stored in an array.
Sample Case 1
Input
5
1 4 6 3 10
Output:
4 6 10
'''
import sys
input_data = sys.stdin.read().strip()
def solve (input_data):
    lines = input_data.split("\n")
    n = int (lines[0])
    nums = list (map(int, lines [1].split()))
    for i in nums:
        if i % 2 == 0:
            print(i, end = " ")

solve(input_data)