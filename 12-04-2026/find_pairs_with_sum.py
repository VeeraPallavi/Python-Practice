'''
Find Pairs with Sum
Description
Given an integer array 'ARR' of size 'N' and an integer 'S', return the list of all pairs of elements such that the sum of each pair equals 'S'. Each pair should be sorted, with the first value less than or equal to the second value. The list of pairs should be sorted in non-decreasing order of their first values, and In case of tles, the pair with the smaller second value should come first.
Input Format:
The first line contains two integers N and S, where N is the size of the array 'ARR' and S is the required sum.
The second line contains N space-separated integers representing the array 'ARR'.
Output Format:
Print each pair on a new line, where each pair consists of two integers separated by a space.
Sample Case 1
Input :
5 5 
1 2 3 4 5
Output:
1 4
2 3
'''
import sys
input_data = sys.stdin.read().strip()
def solve (input_data):
    lines = input_data.split("\n")
    sizes = list (map (int, lines[0].split()))
    n,s = sizes [0], sizes [1]
    nums = sorted (list (map (int, lines [1].split())))
    for i in range(0, n-1):
        for j in range(i+1,n):
            if (nums[i]+nums[j]) == s:
                print (nums[i],nums[j])
                
solve (input_data) 