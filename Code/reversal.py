usr_word = input("Word: ")
words = set(usr_word)

usr_sentence = input("Sentence: ")
sentences = set(usr_sentence)

def reverse_words():
    """
    Desc: Reverse words given by a user 
    Params: None
    Return: Reverse Words
    """
    for _ in words:
        return ' '.join(reversed(usr_word))

# ------------------------
def reverse_sentences():
    """
    Desc: Reverse sentence given by a user 
    Params: None
    Return: Reverse sentence
    """
    for _ in sentences:
        return ' '.join(reversed(usr_sentence))

if __name__ == '__main__':
    reverse_word = reverse_words()
    reverse_sentence = reverse_sentences()

    print(reverse_word)
    print(reverse_sentence)
