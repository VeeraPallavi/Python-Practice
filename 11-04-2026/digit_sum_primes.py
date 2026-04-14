'''
Prime Numbers and Digit Sum Primes
Description:
Write a program that prints all prime numbers and also non-prime numbers If sum of digits is a prime number starting from 1 to n.
Input Format:
A single integer n where 1 ≤ n ≤ 10^6.
Output Format:
Print all prime numbers from 1 to n, each on a new line.
Sample Case 1
Input:
10
Output
2
3
5
7
'''
import sys
input_data = sys.stdin.read().strip()

def isPrime(n):
    if n == 0 or n == 1:
        return False
    for i in range (2, int (n**0.5)+1):
        if n % i == 0:
            return False
    return True

def sumofDigits (n):
    sum_digits = 0
    while n != 0:
        rem=n% 10
        sum_digits += rem
        n=n//10
    return sum_digits

def solve (input_data):
    lines = input_data.split("\n")
    n = int (lines[0])
    for i in range(1,n+1):
        if isPrime(i):
            print(i)
        else:
            sum_digits = sumofDigits(i)
            if isPrime (sum_digits):
                print(i)

solve (input_data)