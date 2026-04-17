'''
Find Remainder
Description:
Given two Integers, dividend and divisor, find the remainder when dividend is divided by divisor without using the / or % operators.
Input Format:
The input consists of two integers: dividend and divisor.
Output Format:
Print the remainder when dividend is divided by divisor.
Sample Case 1
Input
17 5
Output:
2
Sample Case 2
Input
23 7
Output:
2
'''
import sys
input_data = sys.stdin.read().strip()
def solve (input_data):
    lines = input_data.split("\n")
    values = list(map(int, lines[0].strip()))
    a = values[0]
    b = values[1]

    while a >= b:
        a = a-b
    
    print(a)

solve(input_data)