'''
Armstrong Numbers in Range
Description:
Given two Integer values n1 and n2, find and print all Armstrong numbers in the range from n1 to n2 (Inclusive). An Armstrong number (or Narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
Input Format:
The first line contains an integer n1 (1 ≤ n1 ≤ 10^6), representing the start of the range.
The second line contains an integer n2 (n1 s n2 ≤ 10^6), representing the end of the range.
Output Format:
Print all Armstrong numbers in the range from n1 to n2, each on a new line.
Sample Case 1
Input:
100 
500
Output:
153
370
371
407
'''
import sys
input_data = sys.stdin.read().strip()
def sumOfDigits(n):
    count = 0
    while n != 0:
        rem = n % 10
        count += 1
        n = n // 10
    return count

def isAmstrong(n):
    num = n
    count = sumOfDigits(n)
    result = 0
    while n != 0:
        rem = n % 10
        result += (rem ** count)
        n = n // 10
    return result == num

def solve (input_data):
    lines = input_data.split("\n") 
    n1 = int (lines [0])
    n2 = int(lines[1])
    for i in range(n1,n2):
        if isAmstrong(i):
            print(i)
        
solve(input_data)