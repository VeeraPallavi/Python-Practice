'''
Sort Risk Items

Description:
Airport security officials have confiscated several item of the passengers at the security check point. All the items have been dumped into a huge box (array). Each item possesses a certain amount of risk[0,1,2]. Here, the risk severity of the items represent an array[] of N number of integer values. The task here is to sort the items based on their levels of risk in the array. The risk values range from 0 to 2.
Input Format:
The first line contains an integer N, the number of items.
Second line contains n space separated integers representing the risk severity (0, 1, ог 2).
Output Format:
Print the sorted array with risk severities separated by spaces.
Sample Case 1:
Input:
7
1 0 2 0 1 0 2
Output:
0 0 0 1 1 2 2 
'''
import sys
input_data = sys.stdin.read().strip()
def solve (input_data):
    lines = input_data.split("\n")
    n = int (lines[0])
    nums = list (map(int, lines [1].split()))
    for i in range(0, n-1):
        for j in range(i+1, n):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j],nums[i]
    print(*nums)

solve(input_data)