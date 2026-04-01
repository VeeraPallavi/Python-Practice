'''
Print Odd Digits
Description
Given a number, print all the odd digits present in it. If there are no odd digits, print-1
Input Format
The input is a single integer n.
Output Format
Print all odd digits in the number. If there are no odd digits, print -1
Sample Case 1
Input:
1234567890
Output:
9 7 5 3 1
Sample Case 2
Input:
24680
output:
-1'''


import sys

# Read input from standard input

input_data = sys.stdin.read().strip()

def solve (input_data):
    lines = input_data.split("\n") # Split input int
    # User writes their logic here
    n = int (lines[0])
    found = True

    while n > 0:
        rem = n % 10
        if rem % 2 != 0:
            print(rem)
            found = False
        n =n // 10
    
    if found :
        print("-1")
#Call the function
solve (input_data)