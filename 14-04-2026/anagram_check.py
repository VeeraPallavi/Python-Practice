'''
Anagram Check
Description:
Given two strings, check if they are anagrams of each other.
Input Format:
The input consists of two lines: First line containing a string, str1.
Second line containing a string, str2.
Output Format:
Print 'anagrams' if str1 and str2 are anagrams of each other; otherwise, print 'not anagrams'.
Sample Case 1
Input:
anagram marganaa
Output:
not anagrams
Sample Case 2
Input:
Listen silent
Output:
anagrams
'''
import sys
input_data = sys.stdin.read().strip()
def solve (input_data):
    lines = input_data.split("\n")
    str1 = str(lines[0]).lower()
    str2 = str(lines[1]).lower()

    if sorted(str1) == sorted(str2):
        print("anagrams")
    else:
        print("not anagrams")