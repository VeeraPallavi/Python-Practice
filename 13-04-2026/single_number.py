'''
Single Number
Description:
You are given a non-empty array of integers 'nums', where every element appears twice except for one unique element. 
Your task is to find that single unique element.
Input Format:
- The first line contains an integer 'n' (size of the array).
- The second line contains 'n' space-separated integers representing the array elements.
Output Format:
- A single integer representing the unique element that appears only once.
Sample Case 1
Input:
5
2 1 2 3 1
Output
3
'''
def find_single_number(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq [num] = 1
    for key, value in freq.items():
        if value == 1:
            return key

def main():
    n = int(input())
    nums = list (map (int, input().split()))
    unique = find_single_number (nums)
    print (unique)

if __name__ == "_main__":
    main()