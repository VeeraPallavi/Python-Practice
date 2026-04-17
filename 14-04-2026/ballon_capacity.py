'''
Balloon Capacity
Description:
You are managing a hot air balloon ride with a maximum weight capacity W.
There is a queue of N people with individual weights. Starting from the front of the queue, you board people one by one until adding the next person would exceed the balloon's weight capacity.
Your task is to calculate the total number of people who can safely board the balloon without exceeding the weight limit.
Input Format:
The first line contains an integer N, the number of people in the queue.
The second line contains N space-Separated integers representing the weights of the people.
The third line contains an integer W, the maximum weight capacity of the balloon.
Output Format:
Print a single integer representing the number of people who can board the balloon without exceeding the weight limit.
Sample Case 1
Input:
5
60 80 40 50 30
200
Output:
3'''

def solution():
    n = int(input())
    weights = list(map(int, input().split()))
    target = int(input())
    current_weight = 0
    count = 0
    for w in weights :
        current_weight += w
        if current_weight <= target:
            count += 1
        else:
            print(count)
            return

solution()