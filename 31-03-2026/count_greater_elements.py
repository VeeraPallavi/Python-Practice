'''
Count Greater Elements

Description

Given an integer array of size N, count the number of elements where each element is greater than all of its preceding elements. The first element should always be included in the count.
Input Format
The first line contains an integer N, the number of iterns. Second line contains n space separated integer representing the value of the array elements.
Output Format
Print the count of elements that are greater than all preceding elements.
Sample Case 1
Input:
5
7 4 8 2 9
Output:
3
'''

n = int(input())
arr = list(map(int, input().split()))
count = 1  
max = arr[0]
for i in range(1, n):
    if arr[i] > max:
        count += 1
        max = arr[i]
print(count)