'''
Vehicle Fine Calculation
Description
Particulate matters are the biggest contributors to Delhi pollution. The main reason behind the increase in the concentration of PMs include vehícle emission by applying Odd Even concept for all types of vehicles. The vehicles with the odd last digit in the registration number will be allowed on roads on odd dates and those with even last digit will on even dates.
Given an Integer array al], contains the last digit of the registration number of N vehicles traveling on date D(a positive integer). The task is to calculate the total fine collected by the traffic police department from the vehicles violating the rules.
Note: For violating the rule, vehicles would be fined as X Rs.
Input Format
First line contains N(number of vechicles)
Second line contains N space separated integers representing
last digits of registration numbers
Third line contains D(date) and X(fine amount)
Output Format
Print the total fine collected based on the date and the list of vehicle last digits. If no fine is collected, print "0".
Sample Case 1

Input:

5 2 3 7
4
12 200
Output 
600
'''
import sys

input_data = sys.stdin.read().strip()

def solve(input_data):
    lines = input_data.split("\n")
    
    N = int(lines[0])
    arr = list(map(int, lines[1].split()))
    D, X = map(int, lines[2].split())
    
    fine_count = 0
    
    for num in arr:
        if D % 2 == 0:
            if num % 2 != 0:
                fine_count += 1
        else:
            if num % 2 == 0:
                fine_count += 1
    
    print(fine_count * X)

solve(input_data)