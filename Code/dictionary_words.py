"""Import necessary libs"""
import random

word_count = int(input("Number: "))

def create_sentence():
    """
    Desc: Create a sentence using random words that are joined together
    Params: None
    Return: New sentence
    """
    # read the words file
    with open("words.txt", "r", encoding="utf-8") as word_path:
        word_content = word_path.read().split()
        # select random set of words from the file
        random_word = random.sample(word_content, k=min(7, word_count))
        # put the # of words together in to a sentence
    return " ".join(random_word)

if __name__ == "__main__":
    random_sentence = create_sentence()
    # output the sentence
    print(random_sentence)
