'''
Prime Subarray
Description:
You are given an array of integers of size n. 
Your task is to find the length of the longest contiguous subarray that contains only prime numbers. 
A prime number is a number greater than 1 that has no divisors other than 1 and Itself.
A subarray is defined as a contiguous part of the array.
Approach: Traverse the array and check each element whether it is prime or not.
Maintain a counter for the current length of consecutive prime numbers. 
If the current element is prime, increment the counter. 
Otherwise, reset the counter to zero. 
Track the maximum length encountered during the traversal. 
Finally, return the maximum length of such a subarray. 
Edge cases: - If no prime numbers exist, retum 0. 
- If all elements are prime, retum n. 
- Single element arrays should be handled correctly.
Input Format:
The first line contains an integer n representing the size of the array. The second line contains n space-separated integers.
Output Format:
Print a single integer representing the length of the longest subarray consisting only of prime numbers.
Sample Case 1
Input:
5
4 6 8 9 10
Output:
0
'''
def isPrime(n):
    if n==1 or n == 0:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def solution():
    n = int(input())
    nums = list(map(int,input().split()))
    count = 0
    max_count = 0
    for i in range(0,n):
        for j in range(i,n):
            if isPrime(nums[j]):
                count += 1
            else:
                if max_count < count:
                    max_count = count
                count = 0
    
    if max_count < count:
        max_count = count
    print(max_count)