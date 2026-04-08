'''Count substrings that contain only digits.'''

def count_digit_substrings(s):
    count = 0
    current = 0
    
    for char in s:
        if char.isdigit():
            current += 1
            count += current
        else:
            current = 0
    
    return count

print(count_digit_substrings("a12b34"))