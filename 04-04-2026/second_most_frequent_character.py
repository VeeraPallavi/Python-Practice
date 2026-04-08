'''Find Second Most Frequent Character'''

from collections import Counter

def second_most_frequent(s):
    freq = Counter(s)
    values = sorted(freq.values(), reverse=True)
    
    second = values[1]
    for k, v in freq.items():
        if v == second:
            return k

print(second_most_frequent("aabbbbccdde"))