'''
Range Sum Calculator
Description:
Write a program that generates a list L. containing numbers from 0 to 10000.
The program should take two integers I and J as input, representing the starting and ending indices of the list.
Your task is to calculate and print the sum of the elements from Index i to J, Inclusive.
Input Format:
Two integers i and j, separated by a space.
Output Format:
A single integer representing the sum of elements from index i to j in the list.
Sample Case 1
Input
3 7
Output:
25

Sample Case 2
Input:
0 10
Output
55
'''
def main():
    values = list(map(int,input().split()))
    n = values[0]
    m = values[1]
    total_sum = 0
    for i in range(n,m+1):
        total_sum += i
    
    print(total_sum)

if __name__ == "__main__":
    main()