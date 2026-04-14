'''
Merge Sorted Arrays
Description:
Given two sorted arrays, merge them into a single sorted array in ascending order.
Input Format:
The first line contains two space-separated integers n and m, the sizes of arrays A and B.
The second line contains n space-separated integers representing the elements of array A.
The third line contains m space-separated integers representing the elements of array B.
Output Format:
Print space-separated integers representing the merged sorted array.
Sample Case 1
Input
3 3
1 3 5
2 4 6
Output:
1 2 3 4 5 6
'''
import sys
input_data = sys.stdin.read().strip()

def solve (input_data):
    lines = input_data.split("\n") 
    sizes = list(map(int,lines[0].split()))
    n,m = sizes[0],sizes[1]
    A = list(map(int, lines[1].split()))
    B = list(map(int, lines[2].split()))
    i = 0
    j = 0
    while (i<n and j<m):
        if A[i] == B[j]:
            print(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            print(A[i])
            i += 1
        else:
            print(B[j])
            j += 1
    while i<n:
        print(A[i])
        i += 1
    while j<m:
        print(B[j])
        j += 1

solve(input_data)