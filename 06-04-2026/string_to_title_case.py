'''Convert first letter of each word to uppercase.'''

def to_title_case(s):
    result = ""
    capitalize = True
    
    for char in s:
        if char == " ":
            result += char
            capitalize = True
        elif capitalize:
            result += char.upper()
            capitalize = False
        else:
            result += char.lower()
    
    return result

print(to_title_case("hello world python"))