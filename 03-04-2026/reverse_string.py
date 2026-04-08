'''Reverse the given string'''

def reverse_words(s):
    return " ".join(s.split()[::-1])

print(reverse_words("I love Python programming"))