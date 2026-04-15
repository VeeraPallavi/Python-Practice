'''
Single Element Once
Description:
You are given a non-empty array of integers 'nurns", where every element appears exactly three times, except for one unique element which appears exactly once. 
Your task is to find the single element that appears only once. If no such element found print-1.
Input Format:
- The first line contains an integer 'n', denoting the size of the array. - The second line contains 'n' space-separated integers representing the array elements.
Output Format:
- Print a single integer representing the element that appears only once. If no such element then print-1.
Sample Case 1
Input:
7
5 7 5 5 3 3 3
Output:
7
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
    for key, value in freq.items():
        if value == 1:
            print(key)
            return
    print("-1")
solution ()