# Implement a higher order markov chain using a file
import random

# -------------------
# Create a markov chain
def create_markov(text, order):
    """
    Desc: Create a markov chain
    Params: text - file, order - previous states or elements
    Return: Markov chain - dictionary
    """
    # Split the text to create sentences
    word = text.split()
    markov = {}

    # Loop through the length of word minus the previous states
    for i in range(len(word) - order):
        # Splice the list starting from i and ending at i + order
        keys = tuple(word[i:i + order])
        # Assign the next word following the sequence of words
        value = word[i + order]

        # If key is not in markov
        if keys not in markov:
            # Create an empty list as the value corresponding to the key in the dictionary
            markov[keys] = []
        # Append the value corresponding to the key in the dictionary
        markov[keys].append(value)
    # return markov chain
    return markov

# ----------------------------
# Generate a random sentence
def generate_sentence(markov, order, length):
    """
    Desc: Generate a random sentence
    Params: markov, order - previous states or elements, length - length of markov chain
    Return: sentence with a space between
    """
    keys = random.choice(list(markov.keys()))
    sentences = list(keys)

    # Loop through the range of length
    for _ in range(length):
        # Choose a random word
        next_words = random.choice(markov[keys])
        # Append a random word to the list
        sentences.append(next_words)
        # Create a tuple with the last elements of sentences
        keys = tuple(sentences[-order:])
    # return sentences
    return ' '.join(sentences)

# -------------------------
# Read text from a file
with open('SherlockHolmes.txt', 'r', encoding='utf-8') as text_file:
    # Read each line in the file
    text_data = text_file.read()

# ---------------------------
# Higher order markov with a file

# Previous state
order = 2
# Create a markov chain using a text file
markov_chain = create_markov(text_data, order)
# Generate a sentence
generated_text = generate_sentence(markov_chain, order, 50)

print(generated_text)
