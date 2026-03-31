'''
Product of Digits
Description
A supermarket maintains a pricing format for all its products. A value N is printed on each product. When the scanner reads the value N on the item, the product of all the digits in the value N is the price of the item. The task here is to design the software such that given the code of any item N the product (multiplication) of all the digits of value should be computed (price).
Input Format
The input is a single integer N, representing the value of the item code.
Output Format
Print the product of all the digits of the number N.
Sample Case 1
Input:
5244
Output:
160
'''
import sys

# Read input from standard input

input_data = sys.stdin.read().strip()

def solve (input_data):
    lines = input_data.split("\n")
    # Split input into lines
    # User writes their logic here
    nums = int(lines [0])
    product = 1
    while (nums > 0):
        rem = nums % 10
        product = product * rem
        nums = nums // 10
    
    print (product)

#Call the function

solve (input_data)