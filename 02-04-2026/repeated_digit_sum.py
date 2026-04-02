'''
Repeated Digit Sum
Description
An intelligence agency has received reports about some threats. The reports consist of numbers in a mysterious method. There is a number "N" and another number "R". Those numbers are studied thoroughly and it is concluded that all digits of the number 'N' are summed up and this action is performed 'R' number of times. The resultant is also a single digit that is yet to be deciphered. The task here is to find the single-digit sum of the given number 'N' by repeating the action 'R' number of times.
If the value of 'R' is 0, print the output as '0'
Input Format
The input consists of two integers: N (positive integer) and R (non-negative integer).
Output Format
Print the single-digit result obtained after R iterations of summing the digits of N.
Sample Case 1
Input:
99 
3
Output 
9'''

import sys

input_data = sys.stdin.read().strip()

def solve(input_data):
    lines = input_data.split()
    
    N = lines[0]
    R = int(lines[1])
    
    if R == 0:
        print(0)
        return
    
    num = N
    
    for _ in range(R):
        digit_sum = 0
        for ch in num:
            digit_sum += int(ch)
        num = str(digit_sum)
    
    print(num)

solve(input_data)