'''
Count digits in a positive integer
Sample Case :
Input:
123456789
Output:
9
'''
import sys
input_data = sys.stdin.read().strip()

def solve (input_data):
    lines = input_data.split("\n") 
    n =int (lines [0])
    count = 0
    while n != 0:
        rem = n % 10
        count += 1
        n = n // 10
    
    print(count)

solve(input_data)