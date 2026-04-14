'''
Odd Occurring Element
Description:
Given an array of integers where every element appears an even number of times except one element that appears an odd number of times, write a Java program to find that odd occurring element in O(log n) time. The array must satisfy the condition that equal elements must appear in pairs, and no element can appear more than two consecutive times. If the input is invalid, print 'Invalid Inpuť.
Input Format:
- The first line contains an integer 'n' (size of the array). - The second line contains 'n' space-separated integers representing the elements of the array.
Output Format:
- Print the odd occurring element if the input is valid. If the input is invalid, print 'Invalid Input".
Sample Case 1
Input:
7
1 1 2 2 3 4 4
Output : 
3
'''
import sys
input_data = sys.stdin.read().strip()

def solve (input_data):
    lines = input_data.split("\n") 
    n =int (lines [0])
    nums = sorted (list (map(int, lines[1].split())))
    if len (nums)!=n:
        print("Invalid Input")
    low = 0
    high = n-1
    while (low < high):
        mid = (low+high)//2
        if mid % 2 == 1:
            mid -= 1
        if nums [mid] == nums [mid+1]:
            low = mid + 2
        else:
            high = mid
    print (nums [low])

solve(input_data)