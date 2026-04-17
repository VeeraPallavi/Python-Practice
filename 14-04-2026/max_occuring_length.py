'''
Max Occurring Length
Description:
Given a sentence with unique words, print the maximum occurring word length and its occurrence count.
Input Format:
The input is a single string S containing unique words separated by spaces.
Output Format:
Print the occurrence and the length of the most frequently occurring word length in the format: occurance: {occurrence), length: (length}.
Sample Case 1
Input:
alex bob jhon jack ali kelly
Output
occurance: 3 length: 4
Sample Case 2
Input:
openai gpt chat modell
Output:
occurance: 2 length: 6
'''

import sys
input_data = sys.stdin.read().strip()
def solve (input_data):
    lines = input_data.split("\n")
    words = list(map(str, lines [0].split()))
    length_count = {}
    for word in words:
        length = len (word)
        if length in length_count:
            length_count [length] += 1
        else:
            length_count [length] = 1
    max_length = 0
    max_occurence = 0
    for key, value in length_count.items():
        if value > max_occurence:
            max_occurence = value
            max_length = key
    print (f"occurance: (max_occurence)\nlength: (max_length)")

solve(input_data)