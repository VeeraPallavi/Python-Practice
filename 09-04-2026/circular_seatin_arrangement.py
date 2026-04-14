'''
Circular Seating Arrangement
Description:
An International round table conference will be held in india. Presidents from all over the world representing their respective countries will be attending the conference. The task is to find the possible number of ways(P) to make the N members sit around the circular table such that.
The president and prime minister of India will always sit next to each other.
Input Format:
The input is a single integer N representing the number of members.
Output Format:
Print the number of possible seating arrangements where the two specified members are always next to each other.
Sample Case 1
Input:
4
Output:
12
Sample Case 2
Input: 
10
Output:
725760
'''
import sys
input_data = sys.stdin.read().strip()

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def solve (input_data):
    lines = input_data.split("\n")
    n = int (lines[0])
    res = factorial(n-1) * 2
    print(res)

solve(input_data)