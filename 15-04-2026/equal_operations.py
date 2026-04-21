'''
Equal Numbers Operations
Description
You are given three integers (p, q, r). You can perform the following operation any number of times: select two numbers and decrease both by 1, while increasing the third number (not selected) by 2. The task is to determine the minimum number of operations required to make all three integers equal or return -1 if it's not possible.
Input Format:
Three space-separated integers p, q, r.
Output Format:
An integer denoting the minimum number of operations required, or -1 if it cannot be achieved.
Sample Case 1
Input
3 7 5
Output:
2
'''
def solution():
    nums = list(map(int,input().split()))
    p,q,r = nums[0],nums[1],nums[2]
    total = p+q+r
    if total%3 != 0:
        print(-1)
    else:
        target = total//3
        operations = 0
        if p > target:
            operations += p-target
        if q > target:
            operations += q-target
        if r > target:
            operations += r-target
        print(operations)