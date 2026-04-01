'''
Sum of Odd Digits
Description
Given an Integer value n, print the sum of odd digits present in n.
Input Format
The input is a single integer n.
Output Format
Print the sum of odd digits present in n.
Sample Case 1
Input
1234567890
Output:
25
Sample Case 2
Input
24680
Output:
0'''


import sys

# Read input from standard input

input_data = sys.stdin.read().strip()

def solve (input_data):
    lines = input_data.split("\n") # Split input int
    # User writes their logic here
    n = int (lines[0])
    sum = 0

    while n > 0:
        rem = n % 10
        if rem % 2 != 0:
            sum += rem
        n =n // 10
    
    print(sum)
#Call the function
solve (input_data)