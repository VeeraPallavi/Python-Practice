'''Find the first non repeating character from a given string'''

def first_unique_char(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None

print(first_unique_char("aabbcde"))