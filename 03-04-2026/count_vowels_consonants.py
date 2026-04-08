'''count vowels and consonants in a given string'''

def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    v_count = c_count = 0
    
    for char in s:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
                
    return v_count, c_count

print(count_vowels_consonants("Hello World"))