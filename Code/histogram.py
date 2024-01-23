"""Open file"""
txt_file = "DrJekyllandMrHyde.txt"

def load_file():
    """
    Desc: Load the file name or contents of the file 
    Args: source_text, file name or contents of the file as a string
    Return: None
    """
    with open(txt_file, "r", encoding="utf-8") as source_text:
        read_lines = source_text.read().splitlines()
    print(read_lines)

load_file()


# -------------------
def word_frequency():
    """
    Desc: return the total count of unique words when given a word and histogram
    Arguments: word and histogram, ex: "mystery" will 20
    Return: number of times that word appears in a text
    """
    histogram = {}
    for word in txt_file:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    print(histogram)

word_frequency()

# -------------------
def unique_words():
    """
    Desc: return the total count of unique words as an argument
    Args: count, integer from counting the unique words
    Return: Total count of unique words from histogram()
    """
    print(f"Total amount of unique words: {len(txt_file)}")

unique_words()
