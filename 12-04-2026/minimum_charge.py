'''
Minimum Charge
Description:
You are given an integer X which represents the minimum charge required for a laptop to function.
You are also given a list of integers representing the charge levels of different laptops.
The task is to determine how many laptops have a charge greater than or equal to X.
To solve this, Iterate through each element in the list and compare it with X. If the charge value is greater than or equal to X, Increment a counter. Finally, print the total count of such laptops.
Input Format:
First line contains: An integer X-minimum required charge. Second line contains: Space-separated integers charge levels of laptops
Output Format:
Print a single integer - number of laptops that can function
Sample Case 1
Input:
5
5 5 5 5 
Output:
4
'''
def solution():
    n = int(input())
    nums = list(map(int, input().split()))
    count = 0
    for num in nums:
        if num >= n:
            count += 1
    print(count)

solution()