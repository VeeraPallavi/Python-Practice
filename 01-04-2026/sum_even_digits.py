'''
Sum of Even Digits
Description
Given a number, calculate the sum of all the even digits present in it.
Input Format
The input is a single integer n.
Output Format
Print the sum of all even digits in the number.
Sample Case 1
Input
1234567890
Output
20
Sample Case 2
Input
12579
Output:
2'''


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
        if rem % 2 == 0:
            sum += rem
        n =n // 10
    
    print(sum)
#Call the function
solve (input_data)

