'''
Print prime numbers between N1 and N2
Sample Case 1:
Input:
12 37
Output:
13 17 19 23 27 29 31 37
'''
import sys
input_data = sys.stdin.read().strip()

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def solve (input_data):
    lines = input_data.split("\n")
    values = list(map(int, lines[0].split()))
    n1 = values[0]
    n2 = values[1]
    for i in range(n1,n2):
        if isPrime(i):
            print(i, end = " ")

solve(input_data)