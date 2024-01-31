"""Import necessary libraries"""
import random
from histogram import txt_file

# -------------------------
def histogram_builder(file_name):
    """
    Desc: Load the file name or contents of the file 
    Args: source_text, file name or contents of the file as a string
    Return: None
    """
    histogram = {}

    with open(file_name, 'r', encoding="utf-8") as text_file:
        text = text_file.read().splitlines()

        for word in text:
            histogram[word] =  histogram.get(word, 0) + 1
    return histogram

# --------------------------
def random_words(histogram):
    """
    Desc: Take a histogram and return a single word at random
    Args: histogram, empty dictionary
    Return: Return a word at random
    """
    random_sentence = []

    # Randomly get a word
    words = random.choice(list(histogram.keys()))
    random_sentence.append(words)

    for _ in range(len(words)):
        words = random.choice(list(histogram.keys()))

        # End the sentence when a . is selected
        if words == '.':
            random_sentence.append('.')
            break
        random_sentence.append(words)

    length = 5
    return ' '.join(random.choices(random_sentence, k=length))

# ---------------------------
def generate_percentage(histogram):
    """
    Desc: Take a histogram and return the percentage 
    Args: histogram: empty dictionary
    Return: Return the percentage of the word
    """
    histogram_list = list(histogram.keys())

    # select random words based on frequency
    word_percentage = random.choices(histogram_list, weights=histogram.values(), k=1)[0]

    # Calculate word percentage 
    word_total = sum(histogram.values())
    count = histogram[word_percentage]
    percentage = (count / word_total) * 100000

    return word_percentage, percentage

if __name__ == '__main__':
    histogram = histogram_builder(txt_file)
    random_word, text_percentage = generate_percentage(histogram)

    for _ in range(5):
        new_sentence = random_words(histogram)
        print(f"{new_sentence.strip()}.", sep='/n')

    print(f"Text Percentage: {text_percentage}%")
