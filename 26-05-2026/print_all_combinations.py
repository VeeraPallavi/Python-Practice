'''
Print All Combinations
Description
Given an array of size n, generate and print all possible combinations of r elements frm the array.
Input Format:
The first line contains two integers n (1 ≤ n ≤ 20) and r(1 ≤ r ≤ n). 
The second line contains n integers, representing the elements of the array.
Output Format:
Print each combination on a new line, with elements seperated by spaces.
Sample Case 1 
Input
4 2
1 2 3 4
Output
1 2 
1 3
1 4
2 3
2 4
3 4
'''
import sys 

input_data = sys.stdin.read().strip()
def generate_combinations(start,current):
    if len(current) == r:
        print(*current)
        return
    
    for i in range(start,n):
        current.append(i)
        generate_combinations(i+1,current)
        current.pop()

def solve(input_data):
    lines = input_data.split("\n")
    global n,r,nums
    n,r = map(int,lines[0].split())
    nums = list(map(int,lines[1].split()))
    generate_combinations(0,[])

solve(input_data)
