'''
Longest Sequence
Description:
You are given an array of integers of size n. Your task is to sort the array and then find the length of the longest sequence of consecutive numbers present in it. A consecutive sequence means numbers that follow each other with a difference of 1 (for example: 3, 4, 5, 6). After sorting the array, traverse it and count the length of consecutive elements. If the current element is exactly one greater than the previous element, increment the current sequence length. If it is equal (duplicate), ignore it. Otherwise, reset the count. 
Keep track of the maximum length found during traversal and retum it. 
Edge cases:
If the array has only one element, return 1.
If no consecutive elements exist, retum.
Duplicates should not break the sequence but should be ignored.
Input Format:
The first line contains an integer n representing the size of the array. The second line contains n space-separated integers.:
Output Format:
Print a single integer representing the length of the longest consecutive sequence.
Sample Case 1
Input:
5
10 5 6 7 8 
Output:
4
'''

def solution():
    n = int(input())
    nums = list(map(int,input().split()))
    nums = sorted(nums)
    count = 1
    max_count = 1
    if n == 1:
        print("1")
        return 
    for i in range(1,n):
        if nums[i] == nums[i-1]:
            continue
        elif nums[i] == nums[i-1]+1:
            count += 1
        else:
            if max_count < count:
                max_count = count
            count += 1
    
    if max_count < count:
        max_count = count
    print(max_count)