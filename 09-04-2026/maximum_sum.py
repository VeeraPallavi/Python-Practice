'''
Input Format:
The first line contains a single integer N representing the number of players.
The second line contains N space-separated integers representing the bid values.
Output Format:
Print a single integer representing the maximum sum of any two distinct players' bid values.
Sample Case 1:
Input:
5 10 40 30 20 50
Output :
90
'''
def solution():
    nums = list(map(int, input().split()))
    max_sum = 0
    sum = 0
    for i in range(0, len (nums)-1):
        for j in range(i+1, len(nums)):
            sum = nums[i] + nums[j]
            if sum > max_sum:
                max_sum = sum
    print (max_sum)
solution()