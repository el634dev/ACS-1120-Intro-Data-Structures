from random import randint

text = "one fish two fish red fish blue fish"

def random_words(histogram):
    """
    Desc: Take a histogram and return a single word at random
    Args: histogram
    Return: Return a word at random
    """
    histogram = {}
    for word in text:
        if word in histogram:
            histogram[word] + 1
        else:
            histogram[word] = 1
    print(histogram)

random_words(text)
