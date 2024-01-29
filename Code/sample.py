"""Import necessary libraries"""
import random

# --------------------------
def random_words(histogram):
    """
    Desc: Take a histogram and return a single word at random
    Args: histogram, empty dictionary
    Return: Return a word at random
    """
    count = sum(histogram.values())

    rand_num = random.randint(1, count)
    word_sum = 0

    for word, freq in histogram.items():
        word_sum += freq
        if word_sum >= rand_num:
            return word

# ---------------------------
def create_sentence(histogram, histo_length):
    """
    Desc: Take a histogram and the length to create a sentence
    Args: histogram: empty dictionary, histo_length: length of histogram
    Return: Return a word at random
    """
    sentences = []

    for _ in range(histo_length):
        # Get a random word
        word = random_words(histogram)
        # Add the word to the list
        sentences.append(word)

    return " ".join(sentences)

if __name__ == '__main__':
    text = {
        "one": 1,
        "two": 1,
        "three": 1,
        "fish": 4,
        "red": 1,
        "blue": 1,
    }

    random_sentence = create_sentence(text, 1)
    values = f"{text[random_sentence]}"
    print("".join(random_sentence + " => " + str(int(values))))
