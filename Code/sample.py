import random

text = "one fish two fish red fish blue fish"

def random_words(histogram):
    """
    Desc: Take a histogram and return a single word at random
    Args: histogram
    Return: Return a word at random
    """
    histogram = {
        "one": 1, 
        "fish": 4,
        "two": 1, 
        "red": 1, 
        "blue": 1
    }
    
    return random.shuffle(histogram)


random_words(text)
