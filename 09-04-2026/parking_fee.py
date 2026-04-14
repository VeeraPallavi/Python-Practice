'''
Parking Fee
Description :
You are designing a smart parking system for a city parking lot. The system calculates the total parking fee based on the number of hours a vehicle is parked.
The pricing is divided into slabs: For the first 2 hours (hours 0 to 2), 100 is charged per hour.
For the next 3 hours (hours 3 to 5), 50 is charged per hour.
For any duration beyond 5 hours, 20 is charged per hour.
The program must take user input for the number of hours parked, compute the total fee accordingly, and print the result in the format 'Total parking fee: '. If the user enters invalid Input (non-numeric), the program should handle it gracefully and print 'Invalid Input".
Input Format:
A single line containing the number of hours the car is parked.
Output Format:
Print the total parking fee in the format: Total parking fee: <Total parking fee> or print 'Invalid Input' if the input is not a valid number.
Sample Case 1
Input : 
1
Output:
Total Parking Fee : 100'''

def solution():
    try :
        hours = int(input())
        if hours <= 0:
            print("Invalid Input")
        else:
            fee = 0
            if hours <= 2:
                fee = fee + hours * 2
            else:
                fee = fee + 2*100
                if hours <= 5:
                    fee = fee + (hours - 2)* 50
                else:
                    fee = fee +  3*50
                    fee = fee +(hours -5)*20
        print(f"Total Parking Fee:{fee}")
    except:
        print("Invalid Input")

solution()