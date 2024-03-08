"""Implement a higher-order markov"""
import random
# from markov import Markov

class HigherOrderMarkov:
    """Higher order markov chain"""
    def __init__(self, order):
        # Previous state
        self.order = order
        # Create a empty dictionary
        self.markov = {}

    # -------------------------
    # Add a corpus
    def add_corpus(self, corpus):
        """
        Desc: Add a new corpus
        Params: self - instance of class, corpus - body of text
        Return: none
        """
        # Loop through the length of word minus the previous states
        for i in range(len(corpus) - self.order):
            # Splice the list starting from i and ending at i + order
            key = tuple(corpus[i:i + self.order])
            # Assign the next word following the sequence of words
            value = corpus[i + self.order]

            # If key is not in markov
            if key not in self.markov:
                # Create an empty dictionary as the value corresponding to the key in the dictionary
                self.markov[key] = {}
            # If value is not in markov
            if value not in self.markov[key]:
                # Assign 1 as the value and key in the dictionary
                self.markov[key][value] = 1
            else:
                # Add 1 to the value and key in the dictionary
                self.markov[key][value] += 1

    # ---------------------------------
    # Generate a corpus
    def generate_corpus(self, length):
        """
        Desc: Generate corpus
        Params: self - instance of class, length - length of markov chain
        Return: Return a body of text
        """
        # Select a random key from a list of keys
        rand_key = random.choice(list(self.markov.keys()))
        keys = list(rand_key)

        # Loop through the range of length
        for _ in range(length):
            # If key is in markov chain
            if rand_key in self.markov:
                # Select a random token from a list of tokens based on their weights
                token = random.choices(list(self.markov[rand_key].keys()),
                        weights=self.markov[rand_key].values())[0]
                # Append the random token to the list of keys
                keys.append(token)
                # Create a tuple with the last elements of sentences
                rand_key = tuple(keys[-self.order:])
            else:
                break
        # Return the list of keys
        return keys

# Higher Order Markov
order = 2
text = "the brown fox jumped over the lazy dog and cow"
# Split sentence
sentence = text.split()

high_order_markov = HigherOrderMarkov(order)
# Add a corpus
high_order_markov.add_corpus(sentence)

generated_sentence = high_order_markov.generate_corpus(10)
print(' '.join(generated_sentence))
