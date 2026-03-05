'''Reverse Words in a Sentence

Problem:
Given a sentence, reverse the order of words.

Sample Input:
Hello world from Python

Sample Output:
Python from world Hello
'''

def reverse_words(sentence):
    words = sentence.split()[::-1]
    for i in words :
        print(i,end = " ")

sentence = input()
reverse_words(sentence)

