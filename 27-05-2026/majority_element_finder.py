'''
Majority Element Finder
Description
You are given an array containing of 'N' inegers. You are task is to find the majority elemnet in the array.
If there is not majority element lement, print '-1'.
A majority element is an element that apperas more than 'floor(N/2)' times in the array.
Input Format:
The fist line contains a integer 'T', the number of testcases.
For each Test Case:
-The first line contains an integer 'N', the size of the array.
-The second line contains 'N', spac-seperated integers representing the elements of arr.
Output Format:
For each test case, print the majority element. If no majority element exists, print '-1'.

Sample Case 1:
Input:
2
5
2 3 9 2 2
4
8 5 1 9
Output:
2
-1
'''

import sys

input_data = sys.stdin.read().strip()

def solve(input_data):
    lines = input_data.split("\n")

    T = int(lines[0].split())
    index = 1
    for t in range(0,T):
        n = int(lines[index].split())
        nums = list(map(int,lines[index+1].split()))
        index += 2
        found = False
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0)+1
        for key,value in freq.items():
            if value > n//2:
                print(key)
                found = True
        if not found :
            print("-1")
    
solve(input_data)
