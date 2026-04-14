'''
Gym Membership Fee
Description:
A gym offers membership plans based on the number of months a person wants to join.
The valid plans are: 1 month ₹1200, 3 months ₹3000, 6 months → ₹6000, 9 months ₹12000, and 12 months ₹15000.
Your task is to read the number of months a person wants to subscribe and print the corresponding fee. If the input does not match any valid plan, print "Invalid Plan'.
Input Format:
A single integer M representing the number of months the person wants subscribe.
Output Format:
Print the fee for the selected plan, or 'Invalid Plan' if the input does not match any valid plan.
Sample Case 1
Input
1
Output
1200
'''
def solution():
    n = int(input())
    valid_plans = {1:1000,3:3000,6:6000,9:12000,12:15000}
    if n not in valid_plans.keys():
        print("Invalid Plan")
    else:
        print(valid_plans[n])

solution()
