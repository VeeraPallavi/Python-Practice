'''
Pair with a Given Sum in a Sorted Array
Descripion:
Given a sorted array of integers and a tarf=get sum, determine if there xist two elements in the array such that their sum is equal to the target sum.
Input Format:
The first line conatins two integers n( 1<=n<=10^5) and target(the target sum).
The second line contains n intgers.
Output Format:
Print 'Yes' if there are two elements whose sum is equal to the target sum; otherwise, print 'No'.

Sample Case 1
Input :
5 9
1 2 3 4 5
Output:
Yes
'''
import sys

input_data = sys.stdin.read().strip()

def solve(input_data):
    lines = input_data.split("\n")
    n,k = map(int,lines[0].split())
    nums = list(map(int,lines[1].split()))
    start, end = 0, n-1
    while(start < end):
        if nums[start]+nums[end] == k:
            print("Yes")
            return
        elif nums[start]+nums[end] > k:
            end -= 1
        elif nums[start]+nums[end] < k:
            start += 1
    print("No")

solve(input_data)