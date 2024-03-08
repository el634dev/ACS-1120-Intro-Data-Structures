# Implement a higher order markov chain using a file
import random

# -------------------
# Create a markov chain
def create_markov(text, order):
    """
    Desc: Create a markov chain
    Params: text - file, order - previous states or elements
    Return: Markov chain
    """
    # Split the text to create sentences
    word = text.split()
    markov = {}

    for i in range(len(word) - order):
        keys = tuple(word[i:i + order])
        value = word[i + order]

        if keys not in markov:
            markov[keys] = []
        markov[keys].append(value)
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

    for _ in range(length):
        next_words = random.choice(markov[keys])
        sentences.append(next_words)
        keys = tuple(sentences[-order:])
    return ' '.join(sentences)

# -------------------------
# Read text from a file
with open('SherlockHolmes.txt', 'r', encoding='utf-8') as text_file:
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
