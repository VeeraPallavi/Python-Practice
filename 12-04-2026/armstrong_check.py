'''
Armstrong Check
Description:
Given a positive integer N, check whether it is an Armstrong number or not.
Input Format:
An integer N (1 <= N <= 10^9) representing the input number.
Output Format:
Print "Armstrong" if N is an Armstrong number, and "Not Armstrong" otherwise. A
Explanation for Armstrong Number:
An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits. 
For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153. 
Similarly, 370 is an Armstrong number because 3^3 + 7^3+ 0^3= 370. 
A single digit number is always an Armstrong number because it satisfies the condition trivially (e.g., 5 is an Armstrong number because 5^1 = 5).
Sample Case 1
Input:
153
Output:
Armstrong
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

def solve (input_data):
    lines = input_data.split("\n") 
    n =int (lines [0])
    num = n
    count = sumOfDigits(n)
    result = 0
    while n != 0:
        rem = n % 10
        result += (rem ** count)
        n = n // 10
    if result == num:
        print("Armstrong")
    else:
        print("Not Armstrong")
        
solve(input_data)