"""Import necessary libraries"""
import random
import sys

word_line = sys.argv[1:]
words = set(word_line)

def rearrange_words():
    """
    Desc: Rearrange words provided as command-line arguments randomly 
    Params: None
    Return: Rearranged words
    """
    for _ in words:
        return ' '.join(random.sample(word_line, len(word_line)))

if __name__ == '__main__':
    rearranged_sentence = rearrange_words()
    print(rearranged_sentence)
