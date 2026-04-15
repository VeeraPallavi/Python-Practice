'''
Two Unique Elements
Description:
You are given a non-empty array of integers nums, where every element appears exactly twice except for two unique elements that appear exactly once each. 
Your task is to find these two unique elements and print them in ascending order.
Input Format:
The first line contains an integer n, the size of the array.
The second line contains n space-separated integers representing the array elements.
Output Format:
Two integers in ascending order, separated by a space, representing the unique elements.
Sample Case 1
Input:
8
1 2 3 2 4 1 5 5
Output:
3 4
'''
def solution():
    n = int (input())
    nums = list (map(int, input().split()))
    freq = {}
    for num in nums:
        if num in freq:
            freq [num] += 1
        else:
            freq [num] = 1
    res = []
    for key, value in freq.items():
        if value == 1:
            res.append(key)
            print(*sorted (res))
solution ()