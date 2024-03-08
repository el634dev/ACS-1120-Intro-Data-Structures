"""Implement a higher-order markov"""
import random
# from markov import Markov

class HigherOrderMarkov:
    """Higher order markov chain"""
    def __init__(self, order):
        self.order = order
        # Create a empty dictionary
        self.markov = {}

    # -------------------------
    # Add a corpus
    def add_corpus(self, corpus):
        """Add a new corpus"""
        for i in range(len(corpus) - self.order):
            key = tuple(corpus[i:i + self.order])
            value = corpus[i + self.order]

            if key not in self.markov:
                self.markov[key] = {}
            if value not in self.markov[key]:
                self.markov[key][value] = 1
            else:
                self.markov[key][value] += 1

    # ---------------------------------
    # Generate a corpus
    def generate_corpus(self, length):
        """Generate corpus"""
        key = random.choice(list(self.markov.keys()))
        corpus = list(key)

        for _ in range(length):
            if key in self.markov:
                token = random.choices(list(self.markov[key].keys()),
                        weights=self.markov[key].values())[0]
                corpus.append(token)
                key = tuple(corpus[-self.order:])
            else:
                break
        return corpus

# Higher Order Markov
order = 2
text = "the brown fox jumped over the lazy dog and cow"
sentence = text.split()

high_order_markov = HigherOrderMarkov(order)
high_order_markov.add_corpus(sentence)

generated_sentence = high_order_markov.generate_corpus(10)
print(' '.join(generated_sentence))
